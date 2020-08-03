import 'package:flutter/material.dart';
import 'package:flutter/widgets.dart';
import 'package:provider/provider.dart';
import 'package:sih_cotton/models/cotton_type.dart';
import 'package:sih_cotton/models/inventory.dart';
import 'package:sih_cotton/models/market_type.dart';
import 'package:sih_cotton/resources/auth_resource.dart';
import 'package:sih_cotton/resources/sell_resource.dart';
import 'package:sih_cotton/values/styles.dart';
import 'package:sih_cotton/values/values.dart';
import 'package:sih_cotton/widgets/text_translator.dart';

class SellScreen extends StatefulWidget {
  @override
  _SellScreenState createState() => _SellScreenState();
}

class _SellScreenState extends State<SellScreen> {
  TextEditingController _quantityController = TextEditingController();
  TextEditingController _sellingPriceController = TextEditingController();
  int _quantity;
  int _sellingPrice;
  CottonType _cottonType;
  MarketType _marketType;
  Future stats;

  @override
  void initState() {
    super.initState();
    Provider.of<SellResource>(context, listen: false)
        .notification
        .stream
        .listen((event) {
      Scaffold.of(context).showSnackBar(SnackBar(
        content: Text(event),
      ));
    });
  }

  void refresh() {
    if (_cottonType != null && _marketType != null) {
      print('Fetching');
      stats = Provider.of<SellResource>(context, listen: false)
          .getStats(cottonType: _cottonType.id, marketType: _marketType.id);
    }
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: Container(
        child: SingleChildScrollView(
          child: Consumer<SellResource>(builder:
              (BuildContext context, SellResource resource, Widget child) {
            return Padding(
              padding: const EdgeInsets.all(16.0),
              child: Column(
                mainAxisAlignment: MainAxisAlignment.spaceBetween,
                crossAxisAlignment: CrossAxisAlignment.stretch,
                children: [
                  buildActionItems(resource),
                  Padding(
                    padding: const EdgeInsets.symmetric(vertical: 4.0),
                    child: buildCottonTypes(resource),
                  ),
                  Padding(
                    padding: const EdgeInsets.symmetric(vertical: 4.0),
                    child: buildMarket(resource),
                  ),
                  buildTextFormField(
                    controller: _quantityController,
                    hint: 'Enter quantity',
                    label: 'Quantity',
                    variable: _quantity != null ? _quantity.toString() : '',
                  ),
                  buildTextFormField(
                    controller: _sellingPriceController,
                    hint: 'Enter selling price',
                    label: 'Selling Price',
                    variable:
                        _sellingPrice != null ? _sellingPrice.toString() : '',
                  ),
                  Center(child: buildPredictedPrices(resource)),
                  Padding(
                    padding: const EdgeInsets.only(top: 12.0, bottom: 4.0),
                    child: FlatButton(
                      color: Values.PRIMARY_COLOR,
                      onPressed: () {
                        _sellingPrice = int.parse(_sellingPriceController.text);
                        _quantity = int.parse(_quantityController.text);
                        resource.sell(
                            userId: Provider.of<AuthResource>(context,
                                    listen: false)
                                .user
                                .id,
                            cottonType: _cottonType.id,
                            market: _marketType.id,
                            sellingPrice: _sellingPrice,
                            quantity: _quantity);
                      },
                      child: Padding(
                        padding: const EdgeInsets.all(16.0),
                        child: TextTranslator('Sell'),
                      ),
                    ),
                  ),
                ],
              ),
            );
          }),
        ),
      ),
    );
  }

  Widget buildActionItems(SellResource resource) {
    return Row(
      mainAxisAlignment: MainAxisAlignment.spaceBetween,
      children: [
        OutlineButton(
          color: Values.PRIMARY_COLOR,
          padding: EdgeInsets.all(0.0),
          onPressed: () async {
            await resource.fetchMyInventory();
            buildOrderItems(resource.myInventory);
            // resource.myOrders;
          },
          child: TextTranslator('My Inventory'),
        ),
      ],
    );
  }

  Widget buildPredictedPrices(SellResource resource) {
    return FutureBuilder(
        future: stats,
        builder: (context, snapshot) {
          if (snapshot.connectionState == ConnectionState.done) {
            return SingleChildScrollView(
              scrollDirection: Axis.horizontal,
              child: resource.stats.length > 0
                  ? DataTable(
                      columns: [
                        DataColumn(label: TextTranslator('Date')),
                        DataColumn(label: TextTranslator('Predicted Price')),
                      ],
                      rows: resource.stats
                          .where((element) => element.period == 'Daily')
                          .map((e) => DataRow(
                                cells: [
                                  DataCell(Text(e.date)),
                                  DataCell(Text(e.prediction)),
                                ],
                              ))
                          .toList(),
                    )
                  : Container(),
            );
          }
          if (snapshot.connectionState == ConnectionState.active ||
              snapshot.connectionState == ConnectionState.waiting) {
            return Center(
              child: CircularProgressIndicator(),
            );
          }
          return Container();
        });
  }

  void buildOrderItems(List<Inventory> inventoryItem) {
    Navigator.of(context).push(new MaterialPageRoute<Null>(
        builder: (BuildContext context) {
          return Scaffold(
            appBar: AppBar(
              backgroundColor: Colors.white,
              title: TextTranslator('My Inventory'),
            ),
            body: SingleChildScrollView(
              child: ListView(
                shrinkWrap: true,
                physics: NeverScrollableScrollPhysics(),
                children: inventoryItem.map((inventory) {
                  return ListTile(
                    leading: Text(
                      inventory.product.cottonType.name,
                      textAlign: TextAlign.center,
                    ),
                    trailing: Text(
                      '₹${inventory.sellingPrice.toString().padLeft(5)}',
                      style: TextStyle(
                          color: Values.ACCENT_COLOR,
                          fontSize: 16.0,
                          fontWeight: FontWeight.w600),
                    ),
                    title: Text(inventory.product.user.firstName),
                    subtitle: Text(
                        '${inventory.stock.toString()} units left in stock.'),
                    // subtitle: Text('${orderItem.stock} units left'),
                  );
                }).toList(),
              ),
            ),
          );
        },
        fullscreenDialog: true));
  }

  Widget buildCottonTypes(SellResource resource) {
    return FutureBuilder(
        future: resource.getCottonTypes(),
        builder: (context, snapshot) {
          if (snapshot.connectionState == ConnectionState.done) {
            return Padding(
              padding: const EdgeInsets.symmetric(vertical: 4.0),
              child: DropdownButton<CottonType>(
                isExpanded: true,
                hint: TextTranslator('Select Cotton Type'),
                onChanged: (cottonType) {
                  setState(() {
                    _cottonType = cottonType;
                  });
                  refresh();
                },
                value: _cottonType,
                items: resource.cottonTypes.map((cottonType) {
                  return DropdownMenuItem<CottonType>(
                    value: cottonType,
                    child: Text(cottonType.name),
                  );
                }).toList(),
              ),
            );
          }
          if (snapshot.connectionState == ConnectionState.active ||
              snapshot.connectionState == ConnectionState.waiting) {
            return Center(child: CircularProgressIndicator());
          }
          return Container();
        });
  }

  Widget buildMarket(SellResource resource) {
    return FutureBuilder(
        future: resource.getMarketTypes(),
        builder: (context, snapshot) {
          if (snapshot.connectionState == ConnectionState.done) {
            return Padding(
              padding: const EdgeInsets.symmetric(vertical: 4.0),
              child: DropdownButton<MarketType>(
                isExpanded: true,
                hint: TextTranslator('Select Market'),
                onChanged: (marketType) {
                  setState(() {
                    _marketType = marketType;
                  });
                  refresh();
                },
                value: _marketType,
                items: resource.marketTypes.map((market) {
                  return DropdownMenuItem<MarketType>(
                    value: market,
                    child: Text(market.name),
                  );
                }).toList(),
              ),
            );
          }
          if (snapshot.connectionState == ConnectionState.active ||
              snapshot.connectionState == ConnectionState.waiting) {
            return Center(child: CircularProgressIndicator());
          }
          return Container();
        });
  }

  Widget buildTextFormField(
      {TextEditingController controller,
      String hint,
      String label,
      String variable,
      TextInputType textInputType,
      bool obscureText = false,
      Function onChanged}) {
    return Padding(
      padding: const EdgeInsets.symmetric(vertical: 8.0),
      child: TextFormField(
        controller: controller,
        keyboardType: textInputType,
        obscureText: obscureText,
        style: Styles.getTextFormFieldStyle(),
        decoration:
            Styles.getTextFormFieldDecoration(hintText: hint, labelText: label),
        onChanged: (value) {
          variable = value;
          onChanged(value);
        },
      ),
    );
  }
}
