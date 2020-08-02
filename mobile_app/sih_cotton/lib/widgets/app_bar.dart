import 'package:flutter/material.dart';
import 'package:flutter/widgets.dart';
import 'package:provider/provider.dart';
import 'package:sih_cotton/resources/auth_resource.dart';
import 'package:sih_cotton/values/values.dart';

class CustomAppBar extends StatefulWidget implements PreferredSizeWidget {
  final bool noTitle;

  CustomAppBar({Key key, this.noTitle = false}) : super(key: key);

  @override
  _CustomAppBarState createState() => _CustomAppBarState();

  @override
  Size get preferredSize => Size.fromHeight(Values.APP_BAR_HEIGHT);
}

class _CustomAppBarState extends State<CustomAppBar> {
  @override
  Widget build(BuildContext context) {
    return SafeArea(
      child: Container(
        color: Values.PRIMARY_COLOR,
        child: Padding(
          padding: const EdgeInsets.symmetric(vertical: 8.0),
          child: Stack(
            children: <Widget>[
              Consumer<AuthResource>(builder:
                  (BuildContext context, AuthResource resource, Widget child) {
                switch (resource.status) {
                  case AuthStatus.Authenticated:
                    return Align(
                        alignment: Alignment.centerRight,
                        child: IconButton(
                          icon: Icon(Icons.person),
                          onPressed: () {
                            showDialog(
                                context: context,
                                builder: (_) {
                                  return AlertDialog(
                                    title: Text('Account'),
                                    content: Text('Sign out of your account?'),
                                    actions: [
                                      FlatButton(
                                        child: Text('No'),
                                        onPressed: () => Navigator.pop(context),
                                      ),
                                      FlatButton(
                                        child: Text('Yes'),
                                        onPressed: () async {
                                          Navigator.pop(context);
                                          await resource.signOut();
                                        },
                                      ),
                                    ],
                                  );
                                });
                          },
                        ));
                  default:
                    Container();
                }
                return Container();
              }),
              widget.noTitle
                  ? Container()
                  : Align(
                      alignment: Alignment.center,
                      child: Text(
                        Values.appName,
                        style: TextStyle(
                            fontFamily: 'PTSans',
                            fontSize: 20.0,
                            fontWeight: FontWeight.w700,
                            color: Values.ACCENT_COLOR),
                      ),
                    ),
            ],
          ),
        ),
      ),
    );
  }
}
