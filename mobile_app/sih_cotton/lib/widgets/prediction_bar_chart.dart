import 'dart:collection';

import 'package:flutter/material.dart';
import 'package:flutter/widgets.dart';
import 'package:sih_cotton/models/cotton_type.dart';
import 'package:sih_cotton/models/market_type.dart';
import 'package:sih_cotton/resources/analysis_resource.dart';
import 'package:charts_flutter/flutter.dart' as charts;
import 'package:sih_cotton/widgets/text_translator.dart';

class PredictionBarChart extends StatefulWidget {
  final AnalysisResource resource;

  PredictionBarChart(this.resource);

  @override
  _PredictionBarChartState createState() => _PredictionBarChartState();
}

class _PredictionBarChartState extends State<PredictionBarChart> {
  MarketType marketType;
  String period;
  HashMap<String, num> stats = HashMap();
  Future load;

  @override
  void initState() {
    super.initState();
    marketType = widget.resource.marketTypes.first;
    period = 'Daily';
    load = refresh();
  }

  Future refresh() async {
    stats.clear();
    await widget.resource.getStats(marketType: marketType.id);
    widget.resource.stats.forEach((element) {
      if (element.period == period) {
        if (stats.containsKey(element.cottonType.name)) {
          stats[element.cottonType.name] += num.parse(element.prediction);
        }
        stats.putIfAbsent(
            element.cottonType.name, () => num.parse(element.prediction));
      }
    });
    setState(() {});
  }

  @override
  Widget build(BuildContext context) {
    return Padding(
      padding: const EdgeInsets.all(20.0),
      child: FutureBuilder(
          future: load,
          builder: (context, snapshot) {
            if (snapshot.connectionState == ConnectionState.done) {
              return buildPredictionStats(widget.resource);
            }
            if (snapshot.connectionState == ConnectionState.active ||
                snapshot.connectionState == ConnectionState.waiting) {
              return Center(
                child: CircularProgressIndicator(),
              );
            }
            return Container();
          }),
    );
  }

  Widget buildPredictionStats(AnalysisResource resource) {
    return SingleChildScrollView(
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.stretch,
        children: [
          buildMarket(resource),
          DropdownButton<String>(
            items: [
              DropdownMenuItem(
                child: Text('Daily'),
                value: 'Daily',
              ),
              DropdownMenuItem(
                child: Text('Weekly'),
                value: 'Weekly',
              ),
              DropdownMenuItem(
                child: Text('Monthly'),
                value: 'Monthly',
              ),
            ],
            onChanged: (value) {
              setState(() => period = value);
              refresh();
            },
            value: period,
          ),
          Card(
              child: Padding(
            padding: const EdgeInsets.all(8.0),
            child: getBarChart(resource),
          )),
          Divider(),
          Card(child: buildPredictedPrices(resource)),
        ],
      ),
    );
  }

  Widget buildPredictedPrices(AnalysisResource resource) {
    return stats.length > 0
        ? DataTable(
            columns: [
              DataColumn(label: TextTranslator('Date')),
              DataColumn(label: TextTranslator('Average Predicted Price')),
            ],
            rows: stats.entries
                .map((e) => DataRow(
                      cells: [
                        DataCell(Text(e.key)),
                        DataCell(Text((e.value / 7).toStringAsFixed(2))),
                      ],
                    ))
                .toList(),
          )
        : Container();
  }

  Widget getBarChart(AnalysisResource resource) {
    if (marketType == null) {
      return Container(
        child: Text('Select Market Type'),
      );
    }
    print('Here');
    return SizedBox(
      height: 300.0,
      child: SingleChildScrollView(
        scrollDirection: Axis.horizontal,
        child: SizedBox(
          width: MediaQuery.of(context).size.width * 0.9,
          height: 300.0,
          child: charts.BarChart([
            charts.Series<MapEntry<String, num>, String>(
              id: 'Prediction',
              colorFn: (_, __) => charts.MaterialPalette.blue.shadeDefault,
              domainFn: (MapEntry<String, num> sales, _) {
                return sales.key;
              },
              measureFn: (MapEntry<String, num> sales, _) {
                return sales.value / 7;
              },
              data: stats.entries.toList(),
            ),
          ],
              primaryMeasureAxis: new charts.NumericAxisSpec(
                  tickProviderSpec: new charts.BasicNumericTickProviderSpec(
                      desiredTickCount: 10))),
        ),
      ),
    );
  }

  Widget buildMarket(AnalysisResource resource) {
    return FutureBuilder(
        future: load,
        builder: (context, snapshot) {
          if (snapshot.connectionState == ConnectionState.done) {
            return Padding(
              padding: const EdgeInsets.symmetric(vertical: 4.0),
              child: DropdownButton<MarketType>(
                isExpanded: true,
                hint: Text('Select Market'),
                onChanged: (marketType) {
                  setState(() {
                    this.marketType = marketType;
                  });
                  refresh();
                },
                value: this.marketType,
                items: resource.marketTypes.map((market) {
                  return DropdownMenuItem<MarketType>(
                    value: market,
                    child: Text(market.name),
                  );
                }).toList(),
              ),
            );
          }
          if (snapshot.connectionState == ConnectionState.active ||
              snapshot.connectionState == ConnectionState.waiting) {
            return Center(child: CircularProgressIndicator());
          }
          return Container();
        });
  }
}
