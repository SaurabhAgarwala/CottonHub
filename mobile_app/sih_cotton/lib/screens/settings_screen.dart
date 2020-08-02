import 'package:flutter/material.dart';
import 'package:flutter/widgets.dart';
import 'package:provider/provider.dart';
import 'package:sih_cotton/resources/analysis_resource.dart';
import 'package:sih_cotton/resources/auth_resource.dart';
import 'package:sih_cotton/screens/profile_screen.dart';
import 'package:sih_cotton/values/values.dart';
import 'package:sih_cotton/widgets/language.dart';
import 'package:sih_cotton/widgets/prediction_bar_chart.dart';
import 'package:sih_cotton/widgets/prediction_chart.dart';
import 'package:sih_cotton/widgets/text_translator.dart';

class SettingsScreen extends StatefulWidget {
  @override
  _SettingsScreenState createState() => _SettingsScreenState();
}

class _SettingsScreenState extends State<SettingsScreen> {
  @override
  Widget build(BuildContext context) {
    return Container(
        child: SingleChildScrollView(
      child: Padding(
        padding: const EdgeInsets.all(16.0),
        child: buildMainSettings(),
      ),
    ));
  }

  Widget buildMainSettings() {
    return Column(
      children: [
        ListTile(
          title: Text('My Profile'),
          onTap: () {
            buildPopup(
              ProfileScreen(),
              'My Profile',
            );
          },
        ),
        ListTile(
          title: Text('FAQ'),
          onTap: () {
            buildPopup(
              Container(),
              'FAQ',
            );
          },
        ),
        ListTile(
          title: Text('Complaints/Feedback'),
          onTap: () {
            buildPopup(
              Container(),
              'Complaints/Feedback',
            );
          },
        ),
        ListTile(
          title: Text('Change Language'),
          onTap: () {
            buildPopup(
              LanguageWidget(),
              'Change Language',
            );
          },
        ),
        ListTile(
          title: Text('Logout'),
          onTap: () {
            showDialog(
                context: context,
                builder: (_) {
                  return AlertDialog(
                    title: TextTranslator('Logout?'),
                    actions: [
                      FlatButton(
                          onPressed: () {
                            Navigator.pop(context);
                          },
                          child: Text('No')),
                      FlatButton(
                          onPressed: () {
                            Provider.of<AuthResource>(context).signOut();
                            Navigator.pop(context);
                          },
                          child: Text('Yes'))
                    ],
                  );
                });
          },
        ),
      ],
    );
  }

  void buildPopup(Widget widget, String title) {
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
