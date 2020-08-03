import 'dart:async';
import 'dart:collection';

import 'package:dio/dio.dart';
import 'package:flutter/widgets.dart';
import 'package:sih_cotton/models/cotton_type.dart';
import 'package:sih_cotton/models/inventory.dart';
import 'package:sih_cotton/models/market_type.dart';
import 'package:sih_cotton/models/order_item.dart';
import 'package:sih_cotton/models/stat.dart';
import 'package:sih_cotton/singleton.dart';

import 'file:///F:/sih_cotton/lib/values/values.dart';

enum AnalysisStatus {
  Uninitialized,
  Loading,
  Loaded,
  Buying,
  Bought,
  NotBought,
  NotLoaded
}

class AnalysisResource extends ChangeNotifier {
  static const String URL_ANALYSIS = '/analysis';
  static const String URL_COTTON_TYPES = '/cottontype';
  static const String URL_COTTON_MARKET = '/market';
  static const String URL_SPECIFIC = '/analysis/specific';
  static const String URL_HEATMAP = '/getheatmap';

  List<Stat> _stats = [];
  List<CottonType> _cottonTypes = [];
  List<MarketType> _marketTypes = [];

  AnalysisStatus _status = AnalysisStatus.Uninitialized;

  AnalysisStatus get status => _status;

  List<Stat> get stats => _stats;
  List<CottonType> get cottonTypes => _cottonTypes;
  List<MarketType> get marketTypes => _marketTypes;

  StreamController<String> _notification = StreamController.broadcast();
  StreamController<String> get notification => _notification;

  Future getStats({int cottonType, int marketType}) async {
    print('getStats');
    setState(AnalysisStatus.Loading);
    HashMap<String, String> params = HashMap();
    if (cottonType != null)
      params.putIfAbsent('cottontype', () => cottonType.toString());
    if (marketType != null)
      params.putIfAbsent('market', () => marketType.toString());
    try {
      Uri uri = Uri.http(Values.DOMAIN, URL_SPECIFIC, params);
      Response response = await Singleton.instance.dio.getUri(uri,
          options: Options(
            responseType: ResponseType.json,
          ));
      List<dynamic> list = response.data;
      print("getStats fetched");
      if (list.length > 0) {
        _stats.clear();
        print("${list.length} stats available");
        list.forEach((element) {
          print(element);
          var inventoryItem = Stat.fromType(element);
          _stats.add(inventoryItem);
        });
        setState(AnalysisStatus.Loaded);
        return;
      }
      setState(AnalysisStatus.NotLoaded);
    } catch (e) {
      print('Error : $e');
      setState(AnalysisStatus.NotLoaded);
    }
    return;
  }

  Future getCottonTypes() async {
    print('getCottonTypes');
    if (cottonTypes.length > 0) {
      return;
    }
    setState(AnalysisStatus.Loading);
    try {
      Uri uri = Uri.http(Values.DOMAIN, URL_COTTON_TYPES);
      Response response = await Singleton.instance.dio.getUri(uri,
          options: Options(
            responseType: ResponseType.json,
          ));
      List<dynamic> list = response.data;
      print("Cottony Types fetched");
      if (list.length > 0) {
        _stats.clear();
        print("${list.length} cotton types available");
        list.forEach((element) {
          _cottonTypes.add(CottonType.fromType(element));
        });
        setState(AnalysisStatus.Loaded);
        _cottonTypes.sort((a, b) {
          return a.name.compareTo(b.name);
        });
        return;
      }
      setState(AnalysisStatus.NotLoaded);
    } catch (e) {
      print('Error : $e');
      setState(AnalysisStatus.NotLoaded);
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

  Future<String> getImage({String state, String year}) async {
    print('getImage');
    try {
      if (state == null && year == null) {
        return '';
      }
      Uri uri = Uri.http(Values.DOMAIN, URL_HEATMAP, {
        'state': state,
        'year': year,
      });
      Response response = await Singleton.instance.dio.getUri(uri,
          options: Options(
            responseType: ResponseType.json,
          ));
      Map<String, dynamic> map = response.data;
      print("Image fetched");
      if (map.containsKey('image')) return map['image'];
    } catch (e) {
      print('Error : $e');
    }
    return '';
  }

  void setState(AnalysisStatus status) {
    _status = status;
    notifyListeners();
  }
}
