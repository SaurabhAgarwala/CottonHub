import 'package:flutter/material.dart';
import 'package:flutter/widgets.dart';
import 'package:provider/provider.dart';
import 'package:sih_cotton/resources/analysis_resource.dart';
import 'package:sih_cotton/resources/buy_resource.dart';
import 'package:sih_cotton/resources/sell_resource.dart';
import 'package:sih_cotton/screens/analysis_screen.dart';
import 'package:sih_cotton/screens/buy_screen.dart';
import 'package:sih_cotton/screens/dashboard_screen.dart';
import 'package:sih_cotton/screens/profile_screen.dart';
import 'package:sih_cotton/screens/sell_screen.dart';
import 'package:sih_cotton/screens/settings_screen.dart';
import 'package:sih_cotton/values/styles.dart';
import 'package:sih_cotton/values/values.dart';
import 'package:sih_cotton/widgets/text_translator.dart';

class HomeScreen extends StatefulWidget {
  @override
  _HomeScreenState createState() => _HomeScreenState();
}

class _HomeScreenState extends State<HomeScreen> {
  int _selectedIndex = 2;

  void refresh() {
    setState(() {});
  }

  @override
  Widget build(BuildContext context) {
    List<String> options = [
      'Buy',
      'Sell',
      'Home',
      'Analysis',
      'Settings',
    ];
    List<Widget> widgets = [
      ChangeNotifierProvider(create: (_) => BuyResource(), child: BuyScreen()),
      ChangeNotifierProvider(
          create: (_) => SellResource(),
          child: SellScreen()),
      DashboardScreen(),
      ChangeNotifierProvider(
          create: (_) => AnalysisResource(), child: AnalysisScreen()),
      SettingsScreen(refresh),
    ];
    return SafeArea(
      child: Scaffold(
        body: NestedScrollView(
          physics: NeverScrollableScrollPhysics(),
          headerSliverBuilder: (context, innerBoxIsScrolled) {
            return <Widget>[
              SliverAppBar(
                expandedHeight: 100.0,
                floating: false,
                pinned: true,
                backgroundColor: Colors.white,
                flexibleSpace: FlexibleSpaceBar(
                  titlePadding: EdgeInsets.only(left: 8.0, bottom: 8.0),
                  title: TextTranslator(
                    options[_selectedIndex],
                    style: Styles.getHeaderTextStyle(fontSize: 28.0),
                  ),
                ),
              ),
            ];
          },
          body: Card(
            elevation: 1.0,
            child: widgets.elementAt(_selectedIndex),
          ),
        ),
        bottomNavigationBar: Container(
          color: Values.COLOR_1,
          child: BottomNavigationBar(
            backgroundColor: Values.COLOR_1,
            selectedItemColor: Values.ACCENT_COLOR,
            unselectedItemColor: Values.COLOR_2,
            onTap: (choice) {
              print(choice);
              setState(() {
                _selectedIndex = choice;
              });
            },
            currentIndex: _selectedIndex,
            items: [
              BottomNavigationBarItem(
                icon: Icon(Icons.shopping_cart),
                title: Text(options[0]),
              ),
              BottomNavigationBarItem(
                  icon: Icon(Icons.attach_money), title: Text(options[1])),
              BottomNavigationBarItem(
                  icon: Icon(Icons.home), title: Text(options[2])),
              BottomNavigationBarItem(
                  icon: Icon(Icons.insert_chart), title: Text(options[3])),
              BottomNavigationBarItem(
                  icon: Icon(Icons.settings), title: Text(options[4])),
            ],
          ),
        ),
      ),
    );
  }
}
