import 'dart:collection';

import 'package:flutter/material.dart';
import 'package:flutter/widgets.dart';
import 'package:sih_cotton/models/cotton_type.dart';
import 'package:sih_cotton/resources/analysis_resource.dart';
import 'package:charts_flutter/flutter.dart' as charts;

class PredictionBarChart extends StatefulWidget {
  final AnalysisResource resource;

  PredictionBarChart(this.resource);

  @override
  _PredictionBarChartState createState() => _PredictionBarChartState();
}

class _PredictionBarChartState extends State<PredictionBarChart> {
  CottonType predictionCottonType;
  String period;
  HashMap<String, num> stats = HashMap();

  @override
  void initState() {
    super.initState();
    predictionCottonType = widget.resource.cottonTypes.first;
    period = 'Daily';
    refresh();
  }

  void refresh() {
    stats.clear();
    widget.resource.stats.forEach((element) {
      if (element.period == period) {
        if (stats.containsKey(element.cottonType.name)) {
          stats[element.cottonType.name] += num.parse(element.prediction);
        }
        stats.putIfAbsent(
            element.cottonType.name, () => num.parse(element.prediction));
      }
    });
  }

  @override
  Widget build(BuildContext context) {
    return Padding(
      padding: const EdgeInsets.all(20.0),
      child: buildPredictionStats(widget.resource),
    );
  }

  Widget buildPredictionStats(AnalysisResource resource) {
    return Column(
      crossAxisAlignment: CrossAxisAlignment.stretch,
      children: [
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
        getBarChart(resource),
      ],
    );
  }

  Widget getBarChart(AnalysisResource resource) {
    if (predictionCottonType == null) {
      return Container(
        child: Text('Select Cotton Type'),
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
}
