import 'package:sih_cotton/models/auth.dart';
import 'package:sih_cotton/models/cotton_type.dart';

class Product {
  int id;
  User user;
  CottonType cottonType;

  Product.fromType(Map<String, dynamic> parsedJson) {
    id = parsedJson['id'];
    user = User.fromType(parsedJson['user']);
    cottonType = CottonType.fromType(parsedJson['cotton_type']);
  }
}
