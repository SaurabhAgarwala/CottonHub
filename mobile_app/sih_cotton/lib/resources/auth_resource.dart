import 'dart:async';

import 'package:dio/dio.dart';
import 'package:flutter/widgets.dart';
import 'package:shared_preferences/shared_preferences.dart';
import 'package:sih_cotton/models/auth.dart';
import 'package:sih_cotton/singleton.dart';

import 'file:///F:/sih_cotton/lib/values/values.dart';

enum AuthStatus {
  Uninitialized,
  Authenticated,
  Authenticating,
  Unauthenticated,
  AccountCreation,
  AccountCreationFailed
}

class AuthResource extends ChangeNotifier {
  static const String URL_SIGN_IN = '/auth/token/login';
  static const String URL_SIGN_UP = '/auth/users/';
  static const String URL_SIGN_OUT = '/auth/token/logout';
  static const String URL_SIGN_IN_OTP = '/otplogin';
  static const String URL_SIGN_IN_OTP_VERIFY = '/verifyotp';
  static const String URL_ME = '/auth/users/me/';

  String _token;
  User _user;

  String get token => _token;
  AuthStatus _status = AuthStatus.Uninitialized;

  AuthStatus get status => _status;

  StreamController<String> _notification = StreamController.broadcast();
  StreamController<String> get notification => _notification;

  User get user => _user;

  Future signIn(String username, String password) async {
    setState(AuthStatus.Authenticating);
    Uri uri = Uri.http(Values.DOMAIN, URL_SIGN_IN);
    try {
      Response response = await Singleton.instance.dio.postUri(uri,
          data: {'username': username, 'password': password},
          options: Options(
            responseType: ResponseType.json,
          ));
      print('here');
      Map<String, dynamic> map = response.data;
      print('map');
      print(response.data);
      print(map.toString());
      if (map.containsKey('auth_token')) {
        print("Auth succeeded and token received is ${map['auth_token']}");
        _token = map['auth_token'];
        (await Singleton.sharedPreferences).setString('token', _token);
        setState(AuthStatus.Authenticated);
        checkLogin();
        return;
      }
      setState(AuthStatus.Unauthenticated);
    } catch (e) {
      print('Error : $e');
      if (e is DioError) {
        if (e.response != null && e.response.data != null) {
          Map<String, dynamic> map = e.response.data;
          if (map.containsKey('non_field_errors')) {
            if (status != AuthStatus.Authenticated) {
              notification.sink.add(map.entries
                  .firstWhere((element) => element.key == 'non_field_errors')
                  .value
                  .first
                  .toString());
            }
          }
        }
      }
      setState(AuthStatus.Unauthenticated);
    }
  }

  void signInOtp(String mobile) async {
    setState(AuthStatus.Authenticating);
    try {
      Uri uri = Uri.http(Values.DOMAIN, URL_SIGN_IN_OTP);
      Response response = await Singleton.instance.dio.postUri(uri,
          data: {'username': mobile},
          options: Options(
            responseType: ResponseType.json,
          ));
      Map<String, dynamic> map = response.data;
      if (map.containsKey('message')) {
        print("Otp sent to $mobile and message received is ${map['message']}");
        notification.sink.add(map.entries
            .firstWhere((element) => element.key == 'message')
            .value
            .toString());
        setState(AuthStatus.Unauthenticated);
        return;
      }
      setState(AuthStatus.Unauthenticated);
    } catch (e) {
      print('Error : $e');
      if (e is DioError) {
        if (e.response != null && e.response.data != null) {
          Map<String, dynamic> map = e.response.data;
          if (map.containsKey('non_field_errors')) {
            if (status != AuthStatus.Authenticated) {
              notification.sink.add(map.entries
                  .firstWhere((element) => element.key == 'non_field_errors')
                  .value
                  .first
                  .toString());
            }
          }
        }
      }
      setState(AuthStatus.Unauthenticated);
    }
  }

  Future signInOtpVerify(String mobile, String otp) async {
    print('signInOtpVerify');
    setState(AuthStatus.Authenticating);
    try {
      Uri uri = Uri.http(Values.DOMAIN, URL_SIGN_IN_OTP_VERIFY);
      Response response = await Singleton.instance.dio.postUri(uri,
          data: {'username': mobile, 'otp': otp},
          options: Options(
            responseType: ResponseType.json,
          ));
      Map<String, dynamic> map = response.data;
      if (map.containsKey('auth_token')) {
        print("Otp verification succeeded for $mobile");
        _token = map['auth_token'];
        (await Singleton.sharedPreferences).setString('token', _token);
        setState(AuthStatus.Authenticated);
        checkLogin();
        return;
      }
      setState(AuthStatus.Unauthenticated);
    } catch (e) {
      print('Error : $e');
      if (e is DioError) {
        if (e.response != null && e.response.data != null) {
          if (e.response.data is Map<String, dynamic>) {
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
      setState(AuthStatus.Unauthenticated);
    }
    return;
  }

  Future checkLogin() async {
    if (user != null) {
      return;
    }
    setState(AuthStatus.Authenticating);
    try {
      Uri uri = Uri.http(Values.DOMAIN, URL_ME);
      String token = (await SharedPreferences.getInstance()).getString('token');
      print('Token already exists $token');
      if (token != null) {
        Response response = await Singleton.instance.dio.getUri(uri,
//            data: {'auth_token': token},
            options: Options(
              responseType: ResponseType.json,
            ));
        Map<String, dynamic> map = response.data;
        if (map.containsKey('id')) {
          print(
              "Auto login successful for ${map.entries.firstWhere((element) => element.key == 'first_name').value}");
          setState(AuthStatus.Authenticated);
          _user = User.fromType(map);
          return;
        }
        setState(AuthStatus.Unauthenticated);
      } else {
        setState(AuthStatus.Unauthenticated);
      }
    } catch (e) {
      print('Error : $e');
      await (await SharedPreferences.getInstance()).remove('token');
      setState(AuthStatus.Unauthenticated);
    }
    return;
  }

  Future signOut() async {
    setState(AuthStatus.Authenticating);
    try {
      Uri uri = Uri.http(Values.DOMAIN, URL_SIGN_OUT);
      Response response = await Singleton.instance.dio.postUri(uri,
          options: Options(
            responseType: ResponseType.json,
          ));
      await (await Singleton.sharedPreferences).remove('token');
      setState(AuthStatus.Unauthenticated);
      _user = null;
      notification.sink.add('Sign out successful!');
    } catch (e) {
      print('Error : $e');
      setState(AuthStatus.Unauthenticated);
    }
  }

  void signUp(
      {String email,
      String username,
      String password,
      String rePassword,
      String firstName,
      String lastName,
      String address,
      String aadhar,
      String pan,
      String gst}) async {
    setState(AuthStatus.AccountCreation);
    try {
      Uri uri = Uri.http(Values.DOMAIN, URL_SIGN_UP);
      Response response = await Singleton.instance.dio.postUri(uri,
          data: {
            'email': email,
            'username': username,
            'password': password,
            're_password': rePassword,
            'first_name': firstName,
            'last_name': lastName,
//            'address': address,
            'aadhar': aadhar,
            'pan': pan,
//            'gst': gst
          },
          options: Options(
            responseType: ResponseType.json,
          ));
      Map<String, dynamic> map = response.data;
      if (map.containsKey('id')) {
        signIn(username, password);
        return;
      }
      setState(AuthStatus.AccountCreationFailed);
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
      setState(AuthStatus.Unauthenticated);
    }
  }

  Future updateProfile(int id,
      {String email,
      String username,
      String firstName,
      String lastName,
      String address,
      String aadhar,
      String pan,
      String gst}) async {
    try {
      Uri uri = Uri.http(Values.DOMAIN, URL_ME);
      Response response = await Singleton.instance.dio.putUri(uri,
          data: {
            'email': email,
            'username': username,
            'first_name': firstName,
            'last_name': lastName,
            'address': address,
            'aadhar': aadhar,
            'pan': pan,
            'gst': gst
          },
          options: Options(
            responseType: ResponseType.json,
          ));
      Map<String, dynamic> map = response.data;
      if (map.containsKey('id')) {
        _user = User.fromType(map);
        notification.sink.add('Profile updated!');
        return;
      } else {
        notification.sink.add('Could not update!');
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
    return;
  }

  void setState(AuthStatus status) {
    _status = status;
    notifyListeners();
  }
}
