import 'package:flutter/widgets.dart';
import 'package:sih_cotton/values/values.dart';
import 'package:translator/translator.dart';

class TextTranslator extends StatelessWidget {
  TextTranslator(this.text, {Key key, this.style}) : super(key: key);
  final TextStyle style;
  final String text;
  final translator = GoogleTranslator();

  @override
  Widget build(BuildContext context) {
    if (Values.targetLanguage == 'en') {
      return Text(
        text,
        textAlign: TextAlign.left,
        style: style,
      );
    }
    return FutureBuilder(
      future: translator.translate(text, from: 'en', to: Values.targetLanguage),
      builder: (_, AsyncSnapshot<Translation> snapshot) {
        if (snapshot.connectionState == ConnectionState.done) {
          return Text(
            snapshot.data.text,
            textAlign: TextAlign.left,
            style: style,
          );
        }
        if (snapshot.connectionState == ConnectionState.active ||
            snapshot.connectionState == ConnectionState.waiting) {
          return Container();
        }
        return Text(
          text,
          textAlign: TextAlign.left,
          style: style,
        );
      },
    );
  }
}
