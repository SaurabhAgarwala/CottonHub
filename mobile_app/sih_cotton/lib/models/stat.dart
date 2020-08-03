import 'package:sih_cotton/models/cotton_type.dart';
import 'package:sih_cotton/models/market_type.dart';

class Stat {
  int id;
  String period;
  String date;
  String prediction;
  String confidenceLower;
  String confidenceUpper;
  String temperature;
  String rainfall;
  String economyIndicator;
  CottonType cottonType;
  MarketType market;

  Stat.fromType(Map<String, dynamic> parsedJson) {
    id = parsedJson['id'];
    period = parsedJson['period'];
    date = parsedJson['date'];
    prediction = parsedJson['prediction'];
    confidenceLower = parsedJson['confidence_lower'];
    confidenceUpper = parsedJson['confidence_upper'];
    temperature = parsedJson['temperature'];
    rainfall = parsedJson['rainfall'];
    economyIndicator = parsedJson['economy_indicator'];
    cottonType = CottonType.fromType(parsedJson['cotton_type']);
    market = MarketType.fromType(parsedJson['market']);
  }
}
