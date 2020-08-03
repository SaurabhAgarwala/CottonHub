import 'package:sih_cotton/models/auth.dart';
import 'package:sih_cotton/models/inventory.dart';

class OrderItem {
  int id;
  Order order;
  Inventory inventory;
  int quantity;

  OrderItem.fromType(Map<String, dynamic> parsedJson) {
    id = parsedJson['id'];
    quantity = parsedJson['quantity'];
    order = Order.fromType(parsedJson['order']);
    inventory = Inventory.fromType(parsedJson['inventory']);
  }
}

class Order {
  int id;
  User user;
  String name;
  String shippingAddress;
  String mobile;
  bool purchased;

  Order.fromType(Map<String, dynamic> parsedJson) {
    id = parsedJson['id'];
    user = User.fromType(parsedJson['user']);
    name = parsedJson['name'];
    shippingAddress = parsedJson['shipping_address'];
    mobile = parsedJson['mobile'];
    purchased = parsedJson['purchased'];
  }
}
