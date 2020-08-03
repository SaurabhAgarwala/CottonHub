import 'package:flutter/material.dart';
import 'package:flutter/widgets.dart';
import 'package:sih_cotton/models/cotton_type.dart';
import 'package:sih_cotton/models/stat.dart';
import 'package:sih_cotton/resources/analysis_resource.dart';
import 'package:charts_flutter/flutter.dart' as charts;

class PredictionChart extends StatefulWidget {
  final AnalysisResource resource;

  PredictionChart(this.resource);

  @override
  _PredictionChartState createState() => _PredictionChartState();
}

class _PredictionChartState extends State<PredictionChart> {
  CottonType predictionCottonType;
  String period;
  List<Stat> stats = [];

  @override
  void initState() {
    super.initState();
    predictionCottonType = widget.resource.cottonTypes.first;
    period = 'Daily';
    refresh();
  }

  void refresh() {
    stats.clear();
    stats = widget.resource.stats
        .where((element) =>
            element.cottonType.id == predictionCottonType.id &&
                element.period == period ??
            'Daily')
        .toList();
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
        buildCottonTypes(resource),
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
        future: resource.getCottonTypes(),
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
}
