import 'package:flutter/widgets.dart';
import 'package:sih_cotton/widgets/text_translator.dart';

class DashboardScreen extends StatefulWidget {
  @override
  _DashboardScreenState createState() => _DashboardScreenState();
}

class _DashboardScreenState extends State<DashboardScreen> {
  @override
  Widget build(BuildContext context) {
    return SingleChildScrollView(
        child: Column(
      children: [
        Padding(
          padding: const EdgeInsets.all(8.0),
          child: TextTranslator(
            """ 
          CottonHub is an e-commerce portal that streamlines and simplifies the purchasing as well as sales of cotton.  It provides a platform for cotton farmers to upload their information and selling price so that customers can easily find suitable cotton in a market near them.""",
            style: getStyle(),
          ),
        ),
        Padding(
          padding: const EdgeInsets.all(8.0),
          child: TextTranslator(""" 
          In addition to its e-commerce facilities, CottonHub features an Artificial Intelligence based solution which calculates the future market trend of cotton sales on the basis of past years data and predicts the price of cotton on a market and variety basis. Farmers may use this as a guideline 
      to price their cotton. """, style: getStyle()),
        ),
        Padding(
          padding: const EdgeInsets.all(8.0),
          child: TextTranslator(""" 
          Cotton is a commodity, which is perhaps the most volatile among all the agricultural commodities traded. Due to high volatality in cotton prices, it is very difficult for farmers to manually guess the future market trend and accordingly strategize their sales so as to compete in the market and increase the volume of the corporation for sustainable growth. Thus, our artificial Intelligence based solution is a critical tool for farmers to bolster their income!""",
              style: getStyle()),
        )
      ],
    ));
  }

  TextStyle getStyle() {
    return TextStyle(
      fontFamily: 'PT Sans',
      fontSize: 16.0,
    );
  }
}
