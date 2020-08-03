import 'dart:collection';

import 'package:flutter/material.dart';
import 'package:flutter/widgets.dart';
import 'package:shared_preferences/shared_preferences.dart';
import 'package:sih_cotton/values/values.dart';
import 'package:sih_cotton/widgets/restart_widget.dart';
import 'package:sih_cotton/widgets/text_translator.dart';

class LanguageWidget extends StatefulWidget {
  @override
  _LanguageWidgetState createState() => _LanguageWidgetState();
}

class _LanguageWidgetState extends State<LanguageWidget> {
  HashMap<String, String> languages = HashMap();
  String selected;

  @override
  void initState() {
    super.initState();
    Future.microtask(() async {
      selected =
          (await SharedPreferences.getInstance()).get('language') ?? 'en';
    });
    languages.putIfAbsent('English', () => 'en');
    languages.putIfAbsent('Hindi', () => 'hi');
    languages.putIfAbsent('Tamil', () => 'ta');
    languages.putIfAbsent('Telugu', () => 'te');
    languages.putIfAbsent('Bengali', () => 'bn');
    languages.putIfAbsent('Marathi', () => 'mr');
    languages.putIfAbsent('Gujrathi', () => 'gu');
    languages.putIfAbsent('Kannanda', () => 'kn');
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: SingleChildScrollView(
        child: Column(
            children: languages.entries
                .map((entry) => Ink(
                      color: selected == entry.value
                          ? Values.SECONDARY_COLOR
                          : Colors.white,
                      child: ListTile(
                        title: TextTranslator(
                          entry.key,
                          style: TextStyle(
                              color: Colors.black87,
                              fontWeight: selected == entry.value
                                  ? FontWeight.bold
                                  : FontWeight.normal),
                        ),
                        selected: entry.value == selected,
                        onTap: () {
                          setState(() => selected = entry.value);
                        },
                      ),
                    ))
                .toList()),
      ),
      bottomNavigationBar: FlatButton(
          onPressed: () async {
            if (selected != Values.targetLanguage) {
              setState(() {
                Values.targetLanguage = selected;
              });
              (await SharedPreferences.getInstance())
                  .setString('language', selected);
              Navigator.pop(context);
            }
          },
          child: TextTranslator('Select')),
    );
  }
}
