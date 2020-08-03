import 'dart:async';

import 'package:dio/dio.dart';
import 'package:flutter/widgets.dart';
import 'package:sih_cotton/models/cotton_type.dart';
import 'package:sih_cotton/models/inventory.dart';
import 'package:sih_cotton/models/market_type.dart';
import 'package:sih_cotton/singleton.dart';

import 'file:///F:/sih_cotton/lib/values/values.dart';

enum SellStatus { Uninitialized, Selling, Sold, NotSold }

class SellResource extends ChangeNotifier {
  static const String URL_SELL = '/sell';
  static const String URL_COTTON_TYPES = '/cottontype';
  static const String URL_COTTON_MARKET = '/market';
  static const String URL_MY_INVENTORY = '/inventory/me/';

  String _token;
  List<CottonType> _cottonTypes = [];
  List<MarketType> _marketTypes = [];
  List<Inventory> _inventory = [];
  List<Inventory> _myInventory = [];

  List<CottonType> get cottonTypes => _cottonTypes;

  List<MarketType> get marketTypes => _marketTypes;

  List<Inventory> get myInventory => _myInventory;
  List<Inventory> get inventory => _inventory;

  StreamController<String> _notification = StreamController.broadcast();

  StreamController<String> get notification => _notification;

  String get token => _token;
  SellStatus _status = SellStatus.Uninitialized;

  SellStatus get status => _status;

  Future getCottonTypes() async {
    if (cottonTypes.length > 0) return;
    print('getCottonTypes');
    try {
      Uri uri = Uri.http(Values.DOMAIN, URL_COTTON_TYPES);
      Response response = await Singleton.instance.dio.getUri(uri,
          options: Options(
            responseType: ResponseType.json,
          ));
      List<dynamic> list = response.data;
      print("Cotton Types fetched");
      if (list.length > 0) {
        _cottonTypes.clear();
        print("${list.length} cotton types available");
        list.forEach((element) {
          _cottonTypes.add(CottonType.fromType(element));
        });
        _cottonTypes.sort((a, b) {
          return a.name.compareTo(b.name);
        });
        return;
      }
    } catch (e) {
      print('Error : $e');
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

  Future fetchMyInventory() async {
    // if (myInventory.length > 0) return;
    print('fetchMyInventory');
    try {
      Uri uri = Uri.http(Values.DOMAIN, URL_MY_INVENTORY);
      Response response = await Singleton.instance.dio.getUri(uri,
          options: Options(
            responseType: ResponseType.json,
          ));
      List<dynamic> list = response.data;
      print("fetchMyInventory fetched");
      if (list.length > 0) {
        _myInventory.clear();
        print("${list.length} inventory items available");
        list.forEach((element) {
          _myInventory.add(Inventory.fromType(element));
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

  Future sell({
    int userId,
    int cottonType,
    int market,
    int quantity,
    int sellingPrice,
  }) async {
    setState(SellStatus.Selling);
    try {
      Uri uri = Uri.http(Values.DOMAIN, URL_SELL);
      Response response = await Singleton.instance.dio.postUri(uri,
          data: {
            'user_uid': userId,
            'cotton_type': cottonType,
            'quantity': quantity,
            'market': market,
            'selling_price': sellingPrice,
          },
          options: Options(
            responseType: ResponseType.json,
          ));
      Map<String, dynamic> map = response.data;
      if (map.containsKey('status')) {
        if (map['status'] == true)
          _notification.add('Success. Item listed');
        else
          _notification.add('Item not listed. Error occured.');
      }
      setState(SellStatus.Sold);
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
      setState(SellStatus.NotSold);
    }
    setState(SellStatus.NotSold);
  }

  void setState(SellStatus status) {
    _status = status;
    notifyListeners();
  }
}
