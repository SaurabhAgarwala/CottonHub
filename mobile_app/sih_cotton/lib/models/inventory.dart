import 'package:sih_cotton/models/product.dart';

class Inventory {
  int id;
  Product product;
  int stock;
  int sellingPrice;
  int msp;

  Inventory.fromType(Map<String, dynamic> parsedJson) {
    id = parsedJson['id'];
    product = Product.fromType(parsedJson['product']);
    stock = parsedJson['quantity'];
    sellingPrice = parsedJson['selling_price'];
    msp = parsedJson['msp'];
  }
}
