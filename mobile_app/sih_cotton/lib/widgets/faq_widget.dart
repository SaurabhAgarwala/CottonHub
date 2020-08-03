import 'dart:collection';

import 'package:dio/dio.dart';
import 'package:flutter/material.dart';
import 'package:flutter/widgets.dart';
import 'package:sih_cotton/models/faq.dart';
import 'package:sih_cotton/singleton.dart';
import 'package:sih_cotton/values/values.dart';
import 'package:sih_cotton/widgets/text_translator.dart';

class FaqWidget extends StatefulWidget {
  @override
  _FaqWidgetState createState() => _FaqWidgetState();
}

class _FaqWidgetState extends State<FaqWidget> {
  static const String URL_FAQ = '/faq';
  Future<List<Faq>> faqs;

  @override
  void initState() {
    super.initState();
    refresh();
  }

  void refresh() async {
    faqs = fetchFaqs();
  }

  Future<List<Faq>> fetchFaqs() async {
    print('fetchFaqs');
    try {
      Uri uri = Uri.http(Values.DOMAIN, URL_FAQ);
      Response response = await Singleton.instance.dio.getUri(uri,
          options: Options(
            responseType: ResponseType.json,
          ));
      List<dynamic> list = response.data;
      List<Faq> local = [];
      print("faqss fetched");
      if (list.length > 0) {
        print("${list.length} faqs available");
        list.forEach((element) {
          local.add(Faq.fromType(element));
        });
        print("${local.length} faqs available");
        return local;
      }
    } catch (e) {
      print('Error : $e');
    }
    return [];
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
        body: RefreshIndicator(
      onRefresh: fetchFaqs,
      child: FutureBuilder(
          future: faqs,
          builder: (context, AsyncSnapshot<List<Faq>> snapshot) {
            print('State');
            print(snapshot.toString());
            if (snapshot.connectionState == ConnectionState.done) {
              print('Snapshot');
              print(snapshot.data.toString());
              if (snapshot.hasData) {
                return Column(
                    children: snapshot.data
                        .map((faq) => ListTile(
                              title: TextTranslator(
                                faq.question,
                                style: TextStyle(
                                  color: Colors.black87,
                                ),
                              ),
                              onTap: () {
                                showDialog(
                                    context: context,
                                    builder: (_) {
                                      return AlertDialog(
                                        title: TextTranslator('FAQ'),
                                        content: Column(
                                          mainAxisSize: MainAxisSize.min,
                                          children: [
                                            TextTranslator(
                                              faq.question,
                                              style: TextStyle(
                                                  fontWeight: FontWeight.bold,
                                                  fontSize: 18.0),
                                            ),
                                            TextTranslator(faq.answer),
                                          ],
                                        ),
                                        actions: [
                                          FlatButton(
                                              onPressed: () {
                                                Navigator.pop(context);
                                              },
                                              child: TextTranslator('Ok'))
                                        ],
                                      );
                                    });
                              },
                            ))
                        .toList());
              }
            }
            if (snapshot.connectionState == ConnectionState.active ||
                snapshot.connectionState == ConnectionState.waiting) {
              return Center(
                child: CircularProgressIndicator(),
              );
            }
            return Center(
              child: TextTranslator('No FAQs'),
            );
          }),
    ));
  }
}
