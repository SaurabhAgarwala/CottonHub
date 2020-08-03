import 'package:flutter/material.dart';

class Values {
  static String targetLanguage = 'en';
  static const DOMAIN = "cotton-forecast.herokuapp.com";
  static const APP_BAR_HEIGHT = 56.0;
  static const PRIMARY_COLOR = Color(0xffb7ce63);
  static const SECONDARY_COLOR = Color(0xffeef1ef);
  static const ACCENT_COLOR = Color(0xff463f3a);
  static const COLOR_1 = Color(0xff7d98a1);
  static const COLOR_2 = Color(0xffa9b4c2);

  static Map<int, Color> primarySwatch = {
    50: PRIMARY_COLOR.withAlpha(25),
    100: PRIMARY_COLOR.withAlpha(50),
    200: PRIMARY_COLOR.withAlpha(75),
    300: PRIMARY_COLOR.withAlpha(100),
    400: PRIMARY_COLOR.withAlpha(125),
    500: PRIMARY_COLOR.withAlpha(150),
    600: PRIMARY_COLOR.withAlpha(175),
    700: PRIMARY_COLOR.withAlpha(200),
    800: PRIMARY_COLOR.withAlpha(225),
    900: PRIMARY_COLOR.withAlpha(250),
  };

  static const String appName = 'CottonHub';
}
