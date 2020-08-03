import 'package:flutter/material.dart';
import 'package:flutter/widgets.dart';
import 'package:provider/provider.dart';
import 'package:sih_cotton/resources/analysis_resource.dart';
import 'package:sih_cotton/widgets/prediction_bar_chart.dart';
import 'package:sih_cotton/widgets/prediction_chart.dart';

class AnalysisScreen extends StatefulWidget {
  @override
  _AnalysisScreenState createState() => _AnalysisScreenState();
}

class _AnalysisScreenState extends State<AnalysisScreen> {
  @override
  Widget build(BuildContext context) {
    return Container(
        child: SingleChildScrollView(
      child: Padding(
        padding: const EdgeInsets.all(16.0),
        child: Consumer<AnalysisResource>(
          builder:
              (BuildContext context, AnalysisResource resource, Widget child) {
            print(resource.status);
            switch (resource.status) {
              case AnalysisStatus.Uninitialized:
                Future.microtask(() async {
                  await resource.getCottonTypes();
                  await resource.getMarketTypes();
                  await resource.getStats();
                });
                return Center(
                    child: Padding(
                  padding: const EdgeInsets.all(8.0),
                  child: CircularProgressIndicator(),
                ));
              case AnalysisStatus.Loading:
                return Center(
                    child: Padding(
                  padding: const EdgeInsets.all(8.0),
                  child: CircularProgressIndicator(),
                ));
                break;
              case AnalysisStatus.Loaded:
                return buildAnalysisMain(resource);
                break;
              default:
                return Center(
                  child: Container(
                    child: Text('Widget missing'),
                  ),
                );
            }
          },
        ),
      ),
    ));
  }

  Widget buildAnalysisMain(AnalysisResource resource) {
    return Column(
      children: [
        ListTile(
          title: Text('Prediction (Daily/Weekly/Monthly)'),
          onTap: () {
            buildPopup(PredictionChart(resource),
                'Prediction for each cotton type', resource);
          },
        ),
        ListTile(
          title: Text('Prediction (all cotton type)'),
          onTap: () {
            buildPopup(PredictionBarChart(resource),
                'Prediction for all cotton type', resource);
          },
        ),
        ListTile(
          title: Text('Heat map'),
        ),
      ],
    );
  }

  void buildPopup(Widget widget, String title, AnalysisResource resource) {
    Navigator.of(context).push(new MaterialPageRoute<Null>(
        builder: (BuildContext context) {
          return Scaffold(
            appBar: AppBar(
              backgroundColor: Colors.white,
              title: Text(title),
            ),
            body: widget,
          );
        },
        fullscreenDialog: true));
  }
}
