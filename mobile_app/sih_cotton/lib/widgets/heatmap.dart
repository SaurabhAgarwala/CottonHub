import 'dart:convert';

import 'package:flutter/material.dart';
import 'package:flutter/widgets.dart';
import 'package:sih_cotton/resources/analysis_resource.dart';

class HeatMapWidget extends StatefulWidget {
  final AnalysisResource resource;

  HeatMapWidget(this.resource);

  @override
  _HeatMapWidgetState createState() => _HeatMapWidgetState();
}

class _HeatMapWidgetState extends State<HeatMapWidget> {
  String state;
  String year;
  Future load;
  String image;
  // File imageFile;

  @override
  void initState() {
    super.initState();
    state = 'National';
    year = '2020';
    load = refresh();
  }

  Future refresh() async {
    image = await widget.resource.getImage(state: state, year: year);
    image = image.replaceAll('\n', '');
    setState(() {});
    // imageFile = File('test.png');
    // imageFile.writeAsBytesSync(decodedBytes);
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
          DropdownButton<String>(
            items: [
              DropdownMenuItem(
                child: Text('National'),
                value: 'National',
              ),
              DropdownMenuItem(
                child: Text('Gujarat'),
                value: 'Gujarat',
              ),
              DropdownMenuItem(
                child: Text('Karnataka'),
                value: 'Karnataka',
              ),
              DropdownMenuItem(
                child: Text('Maharashtra'),
                value: 'Maharashtra',
              ),
              DropdownMenuItem(
                child: Text('Andhra Pradesh'),
                value: 'Andhra Pradesh',
              ),
            ],
            onChanged: (value) {
              setState(() => state = value);
              refresh();
            },
            value: state,
          ),
          DropdownButton<String>(
            items: [
              DropdownMenuItem(
                child: Text('2015'),
                value: '2015',
              ),
              DropdownMenuItem(
                child: Text('2016'),
                value: '2016',
              ),
              DropdownMenuItem(
                child: Text('2017'),
                value: '2017',
              ),
              DropdownMenuItem(
                child: Text('2018'),
                value: '2018',
              ),
              DropdownMenuItem(
                child: Text('2019'),
                value: '2019',
              ),
              DropdownMenuItem(
                child: Text('2020'),
                value: '2020',
              ),
            ],
            onChanged: (value) {
              setState(() => year = value);
              refresh();
            },
            value: year,
          ),
          Card(
              child: Padding(
            padding: const EdgeInsets.all(8.0),
            child: getBarChart(resource),
          )),
          Divider(),
        ],
      ),
    );
  }

  Widget getBarChart(AnalysisResource resource) {
    return FutureBuilder(
        future: load,
        builder: (_, AsyncSnapshot snapshot) {
          if (image == '') return Container();
          if (snapshot.connectionState == ConnectionState.done) {
            return Image.memory(base64Decode(image));
          }
          if (snapshot.connectionState == ConnectionState.active ||
              snapshot.connectionState == ConnectionState.waiting) {
            return Center(
              child: CircularProgressIndicator(),
            );
          }
          return Container();
        });
  }
}
