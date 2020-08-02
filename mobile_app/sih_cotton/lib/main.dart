import 'package:flutter/material.dart';
import 'package:provider/provider.dart';
import 'package:sih_cotton/resources/auth_resource.dart';
import 'package:sih_cotton/resources/buy_resource.dart';
import 'package:sih_cotton/screens/auth_screen.dart';
import 'package:sih_cotton/values/values.dart';

void main() {
  runApp(MultiProvider(providers: [
    ChangeNotifierProvider(
      create: (context) => AuthResource(),
    ),
    ChangeNotifierProvider(
      create: (context) => BuyResource(),
    ),
  ], child: MyApp()));
}

class MyApp extends StatelessWidget {
  // This widget is the root of your application.
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'SIH Cotton Portal',
      theme: ThemeData(
        primarySwatch:
            MaterialColor(Values.PRIMARY_COLOR.value, Values.primarySwatch),
        visualDensity: VisualDensity.adaptivePlatformDensity,
      ),
      home: Scaffold(body: AuthScreen()),
    );
  }
}
