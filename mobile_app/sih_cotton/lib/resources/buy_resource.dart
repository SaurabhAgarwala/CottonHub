import 'dart:async';

import 'package:dio/dio.dart';
import 'package:flutter/widgets.dart';
import 'package:sih_cotton/models/cotton_type.dart';
import 'package:sih_cotton/models/inventory.dart';
import 'package:sih_cotton/models/market_type.dart';
import 'package:sih_cotton/models/order_item.dart';
import 'package:sih_cotton/singleton.dart';

import 'file:///F:/sih_cotton/lib/values/values.dart';

enum BuyStatus {
  Uninitialized,
  Loading,
  Loaded,
  Buying,
  Bought,
  NotBought,
  NotLoaded
}

class BuyResource extends ChangeNotifier {
  static const String URL_INVENTORY = '/inventory';
  static const String URL_COTTON_TYPES = '/cottontype';
  static const String URL_COTTON_MARKET = '/market';
  static const String URL_BUY = '/addtocart/';
  static const String URL_PLACE_ORCE = '/placeorder/';
  static const String URL_MY_ORDERS = '/orderitem/me/';

  String _token;

  String get token => _token;
  List<Inventory> _inventory = [];
  List<CottonType> _cottonTypes = [];
  List<MarketType> _marketTypes = [];
  List<OrderItem> _myOrders = [];
  List<OrderItem> _cart = [];

  BuyStatus _status = BuyStatus.Uninitialized;

  BuyStatus get status => _status;

  List<Inventory> get inventory => _inventory;

  List<CottonType> get cottonTypes => _cottonTypes;
  List<MarketType> get marketTypes => _marketTypes;
  List<OrderItem> get myOrders => _myOrders;
  List<OrderItem> get cart => _cart;

  StreamController<String> _notification = StreamController.broadcast();
  StreamController<String> get notification => _notification;

  Future getInventory() async {
    print('getInventory');
    setState(BuyStatus.Loading);
    try {
      Uri uri = Uri.http(Values.DOMAIN, URL_INVENTORY);
      Response response = await Singleton.instance.dio.getUri(uri,
          options: Options(
            responseType: ResponseType.json,
          ));
      List<dynamic> list = response.data;
      print("Products fetched");
      if (list.length > 0) {
        _inventory.clear();
        print("${list.length} products available");
        list.forEach((element) {
          print(element);
          var inventoryItem = Inventory.fromType(element);
          if (inventoryItem.stock > 0) {
            _inventory.add(inventoryItem);
          }
        });
        setState(BuyStatus.Loaded);
        return;
      }
      setState(BuyStatus.NotLoaded);
    } catch (e) {
      print('Error : $e');
      setState(BuyStatus.NotLoaded);
    }
    return;
  }

  Future getCottonTypes() async {
    print('getCottonTypes');
    if (cottonTypes.length > 0) {
      return;
    }
    setState(BuyStatus.Loading);
    try {
      Uri uri = Uri.http(Values.DOMAIN, URL_COTTON_TYPES);
      Response response = await Singleton.instance.dio.getUri(uri,
          options: Options(
            responseType: ResponseType.json,
          ));
      List<dynamic> list = response.data;
      print("Cottony Types fetched");
      if (list.length > 0) {
        _inventory.clear();
        print("${list.length} cotton types available");
        list.forEach((element) {
          _cottonTypes.add(CottonType.fromType(element));
        });
        setState(BuyStatus.Loaded);
        _cottonTypes.sort((a, b) {
          return a.name.compareTo(b.name);
        });
        return;
      }
      setState(BuyStatus.NotLoaded);
    } catch (e) {
      print('Error : $e');
      setState(BuyStatus.NotLoaded);
    }
    return;
  }

  Future getMarketTypes() async {
    if (marketTypes.length > 0) return;
    print('getMarketTypes');
    try {
      Uri uri = Uri.http(Values.DOMAIN, URL_COTTON_MARKET);
      Response response = await Singleton.instance.dio.getUri(uri,
          options: Options(
            responseType: ResponseType.json,
          ));
      List<dynamic> list = response.data;
      print("Market Types fetched");
      if (list.length > 0) {
        _marketTypes.clear();
        print("${list.length} market types available");
        list.forEach((element) {
          _marketTypes.add(MarketType.fromType(element));
        });
        _marketTypes.sort((a, b) {
          return a.name.compareTo(b.name);
        });
        return;
      }
    } catch (e) {
      print('Error : $e');
    }
    return;
  }

  Future fetchMyOrders() async {
    // if (myOrders.length > 0) return;
    print('myOrders');
    try {
      Uri uri = Uri.http(Values.DOMAIN, URL_MY_ORDERS);
      Response response = await Singleton.instance.dio.getUri(uri,
          options: Options(
            responseType: ResponseType.json,
          ));
      List<dynamic> list = response.data;
      print("myOrders fetched");
      if (list.length > 0) {
        _myOrders.clear();
        print("${list.length} myOrders available");
        list.forEach((element) {
          var orderItem = OrderItem.fromType(element);
          if (orderItem.order.purchased) {
            _myOrders.add(orderItem);
          }
        });
        return;
      }
    } catch (e) {
      print('Error : $e');
      if (e is DioError) {
        if (e.response != null && e.response.data != null) {
          Map<String, dynamic> map = e.response.data;
          if (map.containsKey('non_field_errors')) {
            notification.sink.add(map.entries
                .firstWhere((element) => element.key == 'non_field_errors')
                .value
                .first
                .toString());
          }
        }
      }
    }
    return;
  }

  Future fetchMyCart() async {
    // if (cart.length > 0) return;
    print('fetchMyCart');
    try {
      Uri uri = Uri.http(Values.DOMAIN, URL_MY_ORDERS);
      Response response = await Singleton.instance.dio.getUri(uri,
          options: Options(
            responseType: ResponseType.json,
          ));
      List<dynamic> list = response.data;
      print("cart fetched");
      if (list.length > 0) {
        _cart.clear();
        print("${list.length} cartitems available");
        list.forEach((element) {
          var orderItem = OrderItem.fromType(element);
          if (orderItem.order.purchased != true) {
            _cart.add(orderItem);
          }
        });
        return;
      }
    } catch (e) {
      print('Error : $e');
      if (e is DioError) {
        if (e.response != null && e.response.data != null) {
          Map<String, dynamic> map = e.response.data;
          if (map.containsKey('non_field_errors')) {
            notification.sink.add(map.entries
                .firstWhere((element) => element.key == 'non_field_errors')
                .value
                .first
                .toString());
          }
        }
      }
    }
    return;
  }

  Future<dynamic> addToCart(
      {int userId,
      int cottonType,
      int market,
      int inventoryId,
      int quantity,
      String name,
      String mobile,
      String shippingAddress}) async {
    try {
      Uri uri = Uri.http(Values.DOMAIN, URL_BUY);
      Response response = await Singleton.instance.dio.postUri(uri,
          data: {
            'user_uid': userId,
            'inventory_id': inventoryId,
            'cotton_type': cottonType,
            'quantity': quantity ?? 1,
            'market': market,
            'name': name,
            'mobile': mobile,
            'shipping_address': shippingAddress ?? '',
          },
          options: Options(
            responseType: ResponseType.json,
          ));
      Map<String, dynamic> map = response.data;
      if (map.containsKey('status')) {
        if (map['status'] == true) {
          getInventory();
          return map['order_id'];
        } else
          _notification.add('Could not place the order');
      }
    } catch (e) {
      print('Error : $e');
      if (e is DioError) {
        if (e.response != null && e.response.data != null) {
          Map<String, dynamic> map = e.response.data;
          if (map.containsKey('non_field_errors')) {
            notification.sink.add(map.entries
                .firstWhere((element) => element.key == 'non_field_errors')
                .value
                .first
                .toString());
          }
        }
      }
    }
    return null;
  }

  Future placeOrder({int id}) async {
    try {
      Uri uri = Uri.http(Values.DOMAIN, URL_PLACE_ORCE + '$id/');
      Response response = await Singleton.instance.dio.putUri(uri,
          options: Options(
            responseType: ResponseType.json,
          ));
      Map<String, dynamic> map = response.data;
      if (map.containsKey('status')) {
        if (map['status'] == true) {
          _notification.add('Order placed.');
          getInventory();
        } else
          _notification.add('Could not place the order');
      }
      return;
    } catch (e) {
      print('Error : $e');
      if (e is DioError) {
        if (e.response != null && e.response.data != null) {
          Map<String, dynamic> map = e.response.data;
          if (map.containsKey('non_field_errors')) {
            notification.sink.add(map.entries
                .firstWhere((element) => element.key == 'non_field_errors')
                .value
                .first
                .toString());
          }
        }
      }
    }
  }

  void setState(BuyStatus status) {
    _status = status;
    notifyListeners();
  }
}
