import 'package:flutter/material.dart';
import 'package:sih_cotton/values/values.dart';

class Styles {
  static getTextFormFieldStyle() {
    return TextStyle();
  }

  static getHeaderTextStyle({double fontSize = 36.0}) {
    return TextStyle(
      color: Values.ACCENT_COLOR,
      fontSize: fontSize,
      fontWeight: FontWeight.w700,
    );
  }

  static InputDecoration getTextFormFieldDecoration(
      {String hintText, String labelText}) {
    return InputDecoration(
      labelText: labelText,
      hintText: hintText,
      fillColor: Colors.white,
      border: UnderlineInputBorder(),
      //fillColor: Colors.green
    );
  }
}
