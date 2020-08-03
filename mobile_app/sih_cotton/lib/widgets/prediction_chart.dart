import 'package:flutter/material.dart';
import 'package:flutter/widgets.dart';
import 'package:sih_cotton/models/cotton_type.dart';
import 'package:sih_cotton/models/market_type.dart';
import 'package:sih_cotton/models/stat.dart';
import 'package:sih_cotton/resources/analysis_resource.dart';
import 'package:charts_flutter/flutter.dart' as charts;
import 'package:sih_cotton/widgets/text_translator.dart';

class PredictionChart extends StatefulWidget {
  final AnalysisResource resource;

  PredictionChart(this.resource);

  @override
  _PredictionChartState createState() => _PredictionChartState();
}

class _PredictionChartState extends State<PredictionChart> {
  CottonType predictionCottonType;
  MarketType marketType;
  String period;
  Future load;
  List<Stat> stats = [];
  bool dataTable = false;

  @override
  void initState() {
    super.initState();
    predictionCottonType = widget.resource.cottonTypes.first;
    marketType = widget.resource.marketTypes.first;
    period = 'Daily';
    load = refresh();
  }

  Future refresh() async {
    if (stats.length > 0) {
      if (stats.first.cottonType.id != predictionCottonType.id ||
          stats.first.market.id != marketType.id) {
        await widget.resource.getStats(
            cottonType: predictionCottonType.id, marketType: marketType.id);
        stats = widget.resource.stats
            .where((element) => element.period == period)
            .toList();
        if (stats.length == 0) {
          Scaffold.of(context).showSnackBar(SnackBar(
            content: Text('No data'),
          ));
        }
      }
    } else {
      await widget.resource.getStats(
          cottonType: predictionCottonType.id, marketType: marketType.id);
      stats = widget.resource.stats
          .where((element) =>
              element.cottonType.id == predictionCottonType.id &&
              element.period == period &&
              element.market.id == marketType.id)
          .toList();
      if (stats.length == 0) {
        Scaffold.of(context).showSnackBar(SnackBar(
          content: Text('No data'),
        ));
      }
    }
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
          buildCottonTypes(resource),
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
              DataColumn(label: TextTranslator('Predicted Price')),
            ],
            rows: stats
                .where((element) => element.period == period)
                .map((e) => DataRow(
                      cells: [
                        DataCell(Text(e.date)),
                        DataCell(Text(e.prediction)),
                      ],
                    ))
                .toList(),
          )
        : Container();
  }

  Widget getBarChart(AnalysisResource resource) {
    if (predictionCottonType == null) {
      return Container(
        child: Text('Select Cotton Type'),
      );
    }
    print('${stats.length} item to be displayed');
    print('Here');
    return SizedBox(
      height: 300.0,
      child: SingleChildScrollView(
        scrollDirection: Axis.horizontal,
        child: SizedBox(
          width: MediaQuery.of(context).size.width * 1.5,
          height: 300.0,
          child: charts.TimeSeriesChart([
            charts.Series<Stat, DateTime>(
              id: 'Prediction',
              colorFn: (_, __) => charts.MaterialPalette.blue.shadeDefault,
              domainFn: (Stat sales, _) {
                var date =
                    sales.date.split('-').map((e) => int.parse(e)).toList();
                return DateTime(date[0], date[1], date[2]);
              },
              measureFn: (Stat sales, _) {
                print(sales.prediction);
                return num.parse(sales.prediction);
              },
              measureLowerBoundFn: (stat, index) =>
                  num.parse(stat.confidenceLower),
              measureUpperBoundFn: (stat, index) =>
                  num.parse(stat.confidenceUpper),
              data: stats,
              labelAccessorFn: (stat, index) {
                return '${stat.period}';
              },
            ),
          ],
              defaultRenderer:
                  new charts.LineRendererConfig(includePoints: true),
              primaryMeasureAxis: new charts.NumericAxisSpec(
                  tickProviderSpec: new charts.BasicNumericTickProviderSpec(
                      desiredTickCount: 10))),
        ),
      ),
    );
  }

  Widget buildCottonTypes(AnalysisResource resource) {
    return FutureBuilder(
        future: load,
        builder: (context, snapshot) {
          if (snapshot.connectionState == ConnectionState.done) {
            return Padding(
              padding: const EdgeInsets.symmetric(vertical: 4.0),
              child: DropdownButton<CottonType>(
                isExpanded: true,
                hint: Text('Select Cotton Type'),
                onChanged: (cottonType) {
                  setState(() {
                    print('Cher');
                    predictionCottonType = cottonType;
                    refresh();
                  });
                },
                value: predictionCottonType,
                items: resource.cottonTypes.map((cottonType) {
                  return DropdownMenuItem<CottonType>(
                    value: cottonType,
                    child: Text(cottonType.name),
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
