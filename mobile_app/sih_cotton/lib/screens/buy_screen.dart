import 'package:flutter/material.dart';
import 'package:flutter/widgets.dart';
import 'package:provider/provider.dart';
import 'package:sih_cotton/models/auth.dart';
import 'package:sih_cotton/models/cotton_type.dart';
import 'package:sih_cotton/models/inventory.dart';
import 'package:sih_cotton/models/market_type.dart';
import 'package:sih_cotton/models/order_item.dart';
import 'package:sih_cotton/resources/auth_resource.dart';
import 'package:sih_cotton/resources/buy_resource.dart';
import 'package:sih_cotton/values/styles.dart';
import 'package:sih_cotton/values/values.dart';
import 'package:sih_cotton/widgets/text_translator.dart';

class BuyScreen extends StatefulWidget {
  @override
  _BuyScreenState createState() => _BuyScreenState();
}

class _BuyScreenState extends State<BuyScreen> {
  CottonType selectedCottonType;
  MarketType selectedMarketType;
  TextEditingController _quantityController = TextEditingController();
  int _quantity;

  @override
  void initState() {
    super.initState();
    Provider.of<BuyResource>(context, listen: false)
        .notification
        .stream
        .listen((event) {
      Scaffold.of(context).showSnackBar(SnackBar(
        content: TextTranslator(event),
      ));
    });
  }

  @override
  Widget build(BuildContext context) {
    return Container(
        child: SingleChildScrollView(
      child: Padding(
        padding: const EdgeInsets.all(16.0),
        child: Consumer<BuyResource>(
          builder: (BuildContext context, BuyResource resource, Widget child) {
            print(resource.status);
            switch (resource.status) {
              case BuyStatus.Uninitialized:
                Future.microtask(() async {
                  await resource.getCottonTypes();
                  await resource.getInventory();
                });
                return Center(
                    child: Padding(
                  padding: const EdgeInsets.all(8.0),
                  child: CircularProgressIndicator(),
                ));
              case BuyStatus.Loading:
                return Center(
                    child: Padding(
                  padding: const EdgeInsets.all(8.0),
                  child: CircularProgressIndicator(),
                ));
                break;
              case BuyStatus.Loaded:
                return buyMainWidget(resource);
                break;
              default:
                return Center(
                  child: Container(
                    child: TextTranslator('Widget missing'),
                  ),
                );
            }
          },
        ),
      ),
    ));
  }

  Widget buyMainWidget(BuyResource resource) {
    return Column(
      mainAxisAlignment: MainAxisAlignment.center,
      crossAxisAlignment: CrossAxisAlignment.stretch,
      children: [
        buildActionItems(resource),
        buildCottonTypes(resource),
        // buildMarket(resource),
        buildInventory(resource)
      ],
    );
  }

  Widget buildActionItems(BuyResource resource) {
    return Row(
      mainAxisAlignment: MainAxisAlignment.spaceBetween,
      children: [
        OutlineButton(
          color: Values.PRIMARY_COLOR,
          padding: EdgeInsets.all(0.0),
          onPressed: () async {
            await resource.fetchMyOrders();
            buildOrderItems(resource.myOrders, 'My Orders');
            resource.myOrders;
          },
          child: TextTranslator('My Orders'),
        ),
        OutlineButton(
          padding: EdgeInsets.all(0.0),
          color: Values.PRIMARY_COLOR,
          onPressed: () async {
            await resource.fetchMyCart();
            buildOrderItems(resource.cart, 'Cart',
                button: Container(
                  color: Values.PRIMARY_COLOR,
                  child: Column(
                    mainAxisSize: MainAxisSize.min,
                    children: [
                      Row(
                        mainAxisAlignment: MainAxisAlignment.spaceBetween,
                        // mainAxisSize: MainAxisSize.min,
                        children: [
                          Padding(
                            padding: const EdgeInsets.all(8.0),
                            child: TextTranslator(
                              'Total : ₹${resource.cart.fold(0, (previousValue, element) => previousValue + (element.inventory.sellingPrice * element.quantity))}',
                              style: TextStyle(
                                  fontWeight: FontWeight.bold, fontSize: 18.0),
                            ),
                          ),
                          Padding(
                            padding: const EdgeInsets.all(8.0),
                            child: FlatButton(
                                color: Values.SECONDARY_COLOR,
                                onPressed: () {
                                  resource.cart.forEach((element) async {
                                    await resource.placeOrder(id: element.id);
                                  });
                                  resource.fetchMyCart();
                                },
                                child: TextTranslator('Place Order')),
                          )
                        ],
                      ),
                    ],
                  ),
                ));
            resource.myOrders;
          },
          child: TextTranslator('Cart'),
        )
      ],
    );
  }

  void buildOrderItems(List<OrderItem> orderItems, String label,
      {Widget button}) {
    Navigator.of(context).push(new MaterialPageRoute<Null>(
        builder: (BuildContext context) {
          return Scaffold(
            appBar: AppBar(
              backgroundColor: Colors.white,
              title: TextTranslator(label),
            ),
            body: ListView(
              shrinkWrap: true,
              children: orderItems.map((orderItem) {
                return ListTile(
                  trailing: TextTranslator(
                    '₹${(orderItem.inventory.sellingPrice * orderItem.quantity).toString().padLeft(5)}',
                    style: TextStyle(
                        color: Values.ACCENT_COLOR,
                        fontSize: 18.0,
                        fontWeight: FontWeight.w600),
                  ),
                  title: TextTranslator(
                      orderItem.inventory.product.user.firstName),
                  subtitle:
                      TextTranslator('${orderItem.quantity.toString()} units.'),
                  // subtitle: TextTranslator('${orderItem.stock} units left'),
                );
              }).toList(),
            ),
            bottomNavigationBar: button,
          );
        },
        fullscreenDialog: true));
  }

  Widget buildTextFormField(
      {TextEditingController controller,
      String hint,
      String label,
      String variable,
      TextInputType textInputType,
      bool obscureText = false,
      Function onChanged}) {
    return TextFormField(
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
    );
  }

  Widget buildInventory(BuyResource resource) {
    if (selectedCottonType == null) {
      return Container();
      // return Center(
      //   child: Padding(
      //     padding: const EdgeInsets.symmetric(vertical: 36.0),
      //     child: TextTranslator('Choose a cotton type!'),
      //   ),
      // );
    }
    var list = resource.inventory
        .where((inventory) =>
            inventory.product.cottonType.id == selectedCottonType.id)
        .toList();
    return SingleChildScrollView(
      child: ListView.builder(
          shrinkWrap: true,
          itemCount: list.length,
          physics: NeverScrollableScrollPhysics(),
          padding: EdgeInsets.all(0.0),
          scrollDirection: Axis.vertical,
          itemBuilder: (context, int pos) {
            Inventory inventory = list[pos];
            return ListTile(
              trailing: TextTranslator(
                '₹${inventory.sellingPrice.toString().padRight(5)}',
                style: TextStyle(
                    color: Values.ACCENT_COLOR,
                    fontSize: 18.0,
                    fontWeight: FontWeight.w600),
              ),
              onTap: () {
                showDialog(
                    context: context,
                    builder: (context) {
                      return AlertDialog(
                        title: TextTranslator('Buy'),
                        content: Column(
                            mainAxisSize: MainAxisSize.min,
                            crossAxisAlignment: CrossAxisAlignment.stretch,
                            mainAxisAlignment: MainAxisAlignment.spaceAround,
                            children: [
                              Padding(
                                padding:
                                    const EdgeInsets.symmetric(vertical: 8.0),
                                child: buildTextFormField(
                                  controller: _quantityController,
                                  hint: 'Enter Quantity',
                                  label: 'Quantity',
                                  variable: _quantity != null
                                      ? _quantity.toString()
                                      : '',
                                ),
                              ),
                              Padding(
                                padding: const EdgeInsets.only(top: 8.0),
                                child: FlatButton(
                                  color: Values.PRIMARY_COLOR,
                                  onPressed: () async {
                                    if (_quantityController.text.isNotEmpty) {
                                      _quantity =
                                          int.parse(_quantityController.text);
                                      User user = Provider.of<AuthResource>(
                                              context,
                                              listen: false)
                                          .user;
                                      dynamic id = await resource.addToCart(
                                        userId: user.id,
                                        cottonType: selectedCottonType.id,
                                        inventoryId: inventory.id,
                                        name: user.firstName,
                                        shippingAddress: user.address,
                                        mobile: user.username,
                                        quantity: _quantity,
                                      );
                                      if (id != null) {
                                        await resource.placeOrder(id: id);
                                      }
                                      Navigator.pop(context);
                                    } else {
                                      resource.notification.sink
                                          .add('Enter quantity');
                                    }
                                  },
                                  child: TextTranslator('Buy'),
                                ),
                              ),
                              FlatButton(
                                color: Values.SECONDARY_COLOR,
                                onPressed: () {
                                  if (_quantityController.text.isNotEmpty) {
                                    _quantity =
                                        int.parse(_quantityController.text);
                                    User user = Provider.of<AuthResource>(
                                            context,
                                            listen: false)
                                        .user;
                                    resource.addToCart(
                                      userId: user.id,
                                      cottonType: selectedCottonType.id,
                                      inventoryId: inventory.id,
                                      name: user.firstName,
                                      shippingAddress: user.address,
                                      mobile: user.username,
                                      quantity: _quantity,
                                    );
                                    Navigator.pop(context);
                                    resource.notification.add('Added to cart');
                                  } else {
                                    resource.notification.sink
                                        .add('Enter quantity');
                                  }
                                },
                                child: TextTranslator('Add to Cart'),
                              )
                            ]),
                      );
                    });
              },
              title: TextTranslator(inventory.product.user.firstName),
              subtitle: TextTranslator('${inventory.stock} units left'),
            );
          }),
    );
  }

  Widget buildCottonTypes(BuyResource resource) {
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
                    selectedCottonType = cottonType;
                  });
                },
                value: selectedCottonType,
                items: resource.cottonTypes.map((cottonType) {
                  return DropdownMenuItem<CottonType>(
                    value: cottonType,
                    child: TextTranslator(cottonType.name),
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

  Widget buildMarket(BuyResource resource) {
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
                    selectedMarketType = marketType;
                  });
                },
                value: selectedMarketType,
                items: resource.marketTypes.map((market) {
                  return DropdownMenuItem<MarketType>(
                    value: market,
                    child: TextTranslator(market.name),
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
}
