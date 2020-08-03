import 'package:flutter/material.dart';
import 'package:flutter/widgets.dart';
import 'package:provider/provider.dart';
import 'package:sih_cotton/resources/auth_resource.dart';
import 'package:sih_cotton/screens/buy_screen.dart';
import 'package:sih_cotton/screens/home_screen.dart';
import 'package:sih_cotton/values/styles.dart';
import 'package:sih_cotton/values/values.dart';
import 'package:sih_cotton/widgets/restart_widget.dart';

class AuthScreen extends StatefulWidget {
  AuthScreen({Key key}) : super(key: key);

  @override
  _AuthScreenState createState() => _AuthScreenState();
}

class _AuthScreenState extends State<AuthScreen> {
  bool _signUp = false;
  bool _signInViaOtp = false;
  TextEditingController _emailController = TextEditingController();
  TextEditingController _firstNameController = TextEditingController();
  TextEditingController _lastNameController = TextEditingController();
  TextEditingController _mobileController = TextEditingController();
  TextEditingController _passwordController = TextEditingController();
  TextEditingController _rePasswordController = TextEditingController();
  TextEditingController _aadharController = TextEditingController();
  TextEditingController _panController = TextEditingController();

  String _firstName,
      _email,
      _lastName,
      _mobile,
      _password,
      _rePassword,
      _otp,
      _aadhar,
      _pan;

  @override
  void initState() {
    super.initState();
    Provider.of<AuthResource>(context, listen: false)
        .notification
        .stream
        .listen((event) {
      Scaffold.of(context).showSnackBar(SnackBar(
        content: Text(event),
      ));
    });
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: Center(
        child: Consumer<AuthResource>(
          builder: (BuildContext context, AuthResource resource, Widget child) {
            print(resource.status);
            switch (resource.status) {
              case AuthStatus.Uninitialized:
                Future.microtask(() => resource.checkLogin());
                return CircularProgressIndicator();
              case AuthStatus.AccountCreation:
                return CircularProgressIndicator();
                break;
              case AuthStatus.Authenticating:
                return CircularProgressIndicator();
                break;
              case AuthStatus.Authenticated:
                return RestartWidget(child: HomeScreen());
                break;
              case AuthStatus.Unauthenticated:
                return buildForm(resource);
                break;
              default:
                return Container(
                  child: Text('Widget missing'),
                );
            }
          },
        ),
      ),
    );
  }

  Widget buildForm(AuthResource resource) {
    return SingleChildScrollView(
      child: Padding(
        padding: const EdgeInsets.all(32.0),
        child: Column(
          mainAxisAlignment: MainAxisAlignment.start,
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            Padding(
              padding: const EdgeInsets.only(top: 8.0),
              child: Center(
                child: Container(
                    decoration: BoxDecoration(
                      shape: BoxShape.circle,
                      color: Values.PRIMARY_COLOR,
                    ),
                    height: 100.0,
                    child: Image(
                        width: 500.0,
                        height: 500.0,
                        image:
                            AssetImage('assets/images/logo_transparent.png'))),
              ),
            ),
            Padding(
              padding: const EdgeInsets.only(top: 4.0, bottom: 20.0),
              child: Center(
                child: Text(
                  Values.appName,
                  style: TextStyle(
                      fontFamily: 'PTSans',
                      fontSize: 42.0,
                      fontWeight: FontWeight.w700,
                      color: Values.ACCENT_COLOR),
                ),
              ),
            ),
            _signUp ? signUpForm(resource) : signInForm(resource),
          ],
        ),
      ),
    );
  }

  Form signUpForm(AuthResource resource) {
    return Form(
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.stretch,
        children: <Widget>[
          Row(
            mainAxisAlignment: MainAxisAlignment.spaceBetween,
            children: [
              Flexible(
                child: Padding(
                  padding: const EdgeInsets.only(right: 4.0),
                  child: buildTextFormField(
                      controller: _firstNameController,
                      hint: 'Enter first name',
                      label: 'First Name',
                      variable: _firstName),
                ),
              ),
              Flexible(
                child: Padding(
                  padding: const EdgeInsets.only(left: 4.0),
                  child: buildTextFormField(
                      controller: _lastNameController,
                      hint: 'Enter last name',
                      label: 'Last Name',
                      variable: _lastName),
                ),
              ),
            ],
          ),
          buildTextFormField(
              controller: _mobileController,
              hint: 'Enter phone',
              label: 'Phone',
              variable: _mobile,
              textInputType: TextInputType.emailAddress),
          Row(
            mainAxisAlignment: MainAxisAlignment.spaceBetween,
            children: [
              Flexible(
                child: Padding(
                  padding: const EdgeInsets.only(right: 4.0),
                  child: buildTextFormField(
                      controller: _aadharController,
                      hint: 'Enter Aadhar number',
                      label: 'Aadhar',
                      variable: _aadhar,
                      textInputType: TextInputType.number),
                ),
              ),
              Flexible(
                child: Padding(
                  padding: const EdgeInsets.only(left: 4.0),
                  child: buildTextFormField(
                      controller: _panController,
                      hint: 'Enter PAN number',
                      label: 'PAN',
                      variable: _pan,
                      textInputType: TextInputType.text),
                ),
              ),
            ],
          ),
          buildTextFormField(
              controller: _passwordController,
              hint: 'Enter Password',
              label: 'Password',
              variable: _password,
              obscureText: true),
          buildTextFormField(
              controller: _rePasswordController,
              hint: 'Enter password again',
              label: 'Confirm Password',
              variable: _rePassword,
              obscureText: true),
          Padding(
            padding: const EdgeInsets.only(top: 12.0, bottom: 4.0),
            child: FlatButton(
              color: Values.PRIMARY_COLOR,
              onPressed: () {
                _email = _emailController.text;
                _firstName = _firstNameController.text;
                _lastName = _lastNameController.text;
                _mobile = _mobileController.text;
                _password = _passwordController.text;
                _rePassword = _rePasswordController.text;
                _aadhar = _aadharController.text;
                _pan = _panController.text;
                resource.signUp(
                    email: _email,
                    firstName: _firstName,
                    lastName: _lastName,
                    username: _mobile,
                    password: _password,
                    rePassword: _rePassword,
                    aadhar: _aadhar,
                    pan: _pan);
              },
              child: Padding(
                padding: const EdgeInsets.all(16.0),
                child: Text('Sign Up'),
              ),
            ),
          ),
          FlatButton(
            onPressed: () {
              setState(() {
                _signUp = false;
              });
            },
            child: Padding(
              padding: const EdgeInsets.symmetric(horizontal: 16.0),
              child: Text('Sign in instead?'),
            ),
          )
        ],
      ),
    );
  }

  Form signInForm(AuthResource resource) {
    return Form(
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.stretch,
        children: <Widget>[
          buildTextFormField(
              controller: _mobileController,
              hint: 'Enter phone (Ex: 9876543210)',
              label: 'Phone',
              variable: _mobile,
              textInputType: TextInputType.phone),
          buildTextFormField(
              controller: _passwordController,
              hint: 'Enter Password or OTP',
              label: 'Password / OTP',
              variable: _password,
              obscureText: true),
          Padding(
            padding: const EdgeInsets.only(top: 12.0, bottom: 4.0),
            child: FlatButton(
              color: Values.PRIMARY_COLOR,
              onPressed: () async {
                _mobile = _mobileController.text;
                _password = _passwordController.text;
                _otp = _passwordController.text;
                if (_otp.isNotEmpty) {
                  await resource.signInOtpVerify(_mobile, _otp);
                }
                if (_password.isNotEmpty &&
                    resource.status != AuthStatus.Authenticated) {
                  await resource.signIn(_mobile, _password);
                }
              },
              child: Padding(
                padding: const EdgeInsets.all(16.0),
                child: Text('Sign In'),
              ),
            ),
          ),
          Padding(
            padding: const EdgeInsets.only(top: 8.0, bottom: 4.0),
            child: FlatButton(
              color: Values.SECONDARY_COLOR,
              onPressed: () {
                setState(() {
                  _signInViaOtp = !_signInViaOtp;
                });
                _mobile = _mobileController.text;
                resource.signInOtp(_mobile);
              },
              child: Padding(
                padding: const EdgeInsets.all(16.0),
                child: Text('Get OTP'),
              ),
            ),
          ),
          Divider(color: Values.ACCENT_COLOR, thickness: 0.4),
          FlatButton(
            padding: EdgeInsets.all(0.0),
            onPressed: () {
              setState(() {
                _signUp = true;
              });
            },
            child: Padding(
              padding: const EdgeInsets.symmetric(horizontal: 16.0),
              child: Text('Sign up instead?'),
            ),
          )
        ],
      ),
    );
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
