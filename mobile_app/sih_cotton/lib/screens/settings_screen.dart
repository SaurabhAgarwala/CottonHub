import 'package:dio/dio.dart';
import 'package:flutter/material.dart';
import 'package:flutter/widgets.dart';
import 'package:provider/provider.dart';
import 'package:sih_cotton/resources/analysis_resource.dart';
import 'package:sih_cotton/resources/auth_resource.dart';
import 'package:sih_cotton/screens/profile_screen.dart';
import 'package:sih_cotton/singleton.dart';
import 'package:sih_cotton/values/values.dart';
import 'package:sih_cotton/widgets/faq_widget.dart';
import 'package:sih_cotton/widgets/language.dart';
import 'package:sih_cotton/widgets/text_translator.dart';

class SettingsScreen extends StatefulWidget {
  final Function refresh;

  SettingsScreen(this.refresh);
  @override
  _SettingsScreenState createState() => _SettingsScreenState();
}

class _SettingsScreenState extends State<SettingsScreen> {
  static const String URL_FEEDBACK = '/feedback/';
  static const String URL_COMPLAINT = '/complaint/';
  String subject;
  String body;

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
          title: TextTranslator('My Profile'),
          onTap: () {
            buildPopup(
              ProfileScreen(),
              'My Profile',
            );
          },
        ),
        ListTile(
          title: TextTranslator('Change Language'),
          onTap: () {
            buildPopup(
              LanguageWidget(),
              'Change Language',
            );
          },
        ),
        ListTile(
          title: TextTranslator('FAQ'),
          onTap: () {
            buildPopup(
              FaqWidget(),
              'FAQ',
            );
          },
        ),
        ListTile(
          title: TextTranslator('Register Complaint'),
          onTap: () {
            showDialog(
                context: context,
                builder: (_) {
                  return AlertDialog(
                    title: TextTranslator('Register complaint'),
                    content: Column(
                      mainAxisSize: MainAxisSize.min,
                      children: [
                        TextField(
                          decoration: InputDecoration(hintText: 'Subject'),
                          onChanged: (value) => subject = value,
                        ),
                        TextField(
                          decoration: InputDecoration(hintText: 'Body'),
                          onChanged: (value) => body = value,
                        )
                      ],
                    ),
                    actions: [
                      FlatButton(
                          onPressed: () {
                            Navigator.pop(context);
                          },
                          child: TextTranslator('Cancel')),
                      FlatButton(
                          onPressed: () {
                            postComplaint(subject, body);
                            Navigator.pop(context);
                          },
                          child: TextTranslator('Register'))
                    ],
                  );
                });
          },
        ),
        ListTile(
          title: TextTranslator('Give Feedback'),
          onTap: () {
            showDialog(
                context: context,
                builder: (_) {
                  return AlertDialog(
                    title: TextTranslator('Feedback'),
                    content: Column(
                      mainAxisSize: MainAxisSize.min,
                      children: [
                        TextField(
                          decoration: InputDecoration(hintText: 'Subject'),
                          onChanged: (value) => subject = value,
                        ),
                        TextField(
                          decoration: InputDecoration(hintText: 'Body'),
                          onChanged: (value) => body = value,
                        )
                      ],
                    ),
                    actions: [
                      FlatButton(
                          onPressed: () {
                            Navigator.pop(context);
                          },
                          child: TextTranslator('Cancel')),
                      FlatButton(
                          onPressed: () {
                            postFeedback(subject, body);
                            Navigator.pop(context);
                          },
                          child: TextTranslator('Post'))
                    ],
                  );
                });
          },
        ),
        ListTile(
          title: TextTranslator('Logout'),
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
                          child: TextTranslator('No')),
                      FlatButton(
                          onPressed: () async {
                            await Provider.of<AuthResource>(context,
                                    listen: false)
                                .signOut();
                            Navigator.pop(context);
                          },
                          child: TextTranslator('Yes'))
                    ],
                  );
                });
          },
        ),
      ],
    );
  }

  void buildPopup(Widget customWidget, String title) async {
    await Navigator.of(context).push(new MaterialPageRoute<Null>(
        builder: (BuildContext context) {
          return Scaffold(
            appBar: AppBar(
              backgroundColor: Colors.white,
              title: TextTranslator(title),
            ),
            body: customWidget,
          );
        },
        fullscreenDialog: true));
    widget.refresh();
    setState(() {});
  }

  Future postComplaint(String subject, String body) async {
    print('postComplaint');
    try {
      Uri uri = Uri.http(Values.DOMAIN, URL_COMPLAINT);
      Response response = await Singleton.instance.dio.postUri(uri,
          data: {'subject': subject, 'body': body},
          options: Options(
            responseType: ResponseType.json,
          ));
      Map<String, dynamic> map = response.data;
      if (map.containsKey('id')) {
        print("Post comlpaint succesful");
        Scaffold.of(context).showSnackBar(
            SnackBar(content: TextTranslator('Complaint registered.')));
      }
    } catch (e) {
      print('Error : $e');
      Scaffold.of(context).showSnackBar(
          SnackBar(content: TextTranslator('Could not post complaint')));
    }
    this.subject = null;
    this.body = null;
    return;
  }

  Future postFeedback(String subject, String body) async {
    print('postFeedback');
    try {
      Uri uri = Uri.http(Values.DOMAIN, URL_FEEDBACK);
      Response response = await Singleton.instance.dio.postUri(uri,
          data: {'subject': subject, 'body': body},
          options: Options(
            responseType: ResponseType.json,
          ));
      Map<String, dynamic> map = response.data;
      if (map.containsKey('id')) {
        print("Post feedback succesful");
        Scaffold.of(context).showSnackBar(
            SnackBar(content: TextTranslator('Feedback received.')));
      }
    } catch (e) {
      print('Error : $e');
      Scaffold.of(context).showSnackBar(
          SnackBar(content: TextTranslator('Could not post feedback')));
    }
    this.subject = null;
    this.body = null;
    return;
  }
}
