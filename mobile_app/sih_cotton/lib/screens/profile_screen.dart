import 'package:flutter/material.dart';
import 'package:flutter/widgets.dart';
import 'package:provider/provider.dart';
import 'package:sih_cotton/resources/auth_resource.dart';
import 'package:sih_cotton/values/styles.dart';
import 'package:sih_cotton/values/values.dart';

class ProfileScreen extends StatefulWidget {
  @override
  _ProfileScreenState createState() => _ProfileScreenState();
}

class _ProfileScreenState extends State<ProfileScreen> {
  TextEditingController _emailController = TextEditingController();
  TextEditingController _firstNameController = TextEditingController();
  TextEditingController _lastNameController = TextEditingController();
  TextEditingController _mobileController = TextEditingController();
  TextEditingController _aadharController = TextEditingController();
  TextEditingController _panController = TextEditingController();

  String _firstName, _email, _lastName, _mobile, _aadhar, _pan;

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
    return SingleChildScrollView(
      child: Consumer<AuthResource>(
        builder: (BuildContext context, AuthResource resource, Widget child) {
          print('Profile Screen');
          print(resource.status);
          switch (resource.status) {
            case AuthStatus.Authenticated:
              return buildMyProfile(resource);
            default:
              return Container(
                child: Text('Login first.'),
              );
          }
        },
      ),
    );
  }

  Widget buildMyProfile(AuthResource resource) {
    _emailController.text = resource.user.email;
    _firstNameController.text = resource.user.firstName;
    _lastNameController.text = resource.user.lastName;
    _mobileController.text = resource.user.username;
    _aadharController.text = resource.user.aadhar;
    _panController.text = resource.user.pan;

    return FutureBuilder(
        future: resource.checkLogin(),
        builder: (context, snapshot) {
          if (snapshot.connectionState == ConnectionState.done) {
            return Form(
                child: Padding(
              padding: const EdgeInsets.all(16.0),
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
                      enabled: false,
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
                  Padding(
                    padding: const EdgeInsets.only(top: 12.0, bottom: 4.0),
                    child: FlatButton(
                      color: Values.PRIMARY_COLOR,
                      onPressed: () {
                        _email = _emailController.text;
                        _firstName = _firstNameController.text;
                        _lastName = _lastNameController.text;
                        _mobile = _mobileController.text;
                        _aadhar = _aadharController.text;
                        _pan = _panController.text;
                        resource.updateProfile(resource.user.id,
                            email: _email,
                            firstName: _firstName,
                            lastName: _lastName,
                            username: _mobile,
                            aadhar: _aadhar,
                            pan: _pan);
                      },
                      child: Padding(
                        padding: const EdgeInsets.all(16.0),
                        child: Text('Update'),
                      ),
                    ),
                  ),
                  Padding(
                    padding: const EdgeInsets.only(top: 12.0, bottom: 4.0),
                    child: FlatButton(
                      color: Values.SECONDARY_COLOR,
                      onPressed: () {
                        resource.signOut();
                      },
                      child: Padding(
                        padding: const EdgeInsets.all(16.0),
                        child: Text('Sign Out'),
                      ),
                    ),
                  ),
                ],
              ),
            ));
          }
          if (snapshot.connectionState == ConnectionState.waiting ||
              snapshot.connectionState == ConnectionState.active) {
            return Center(
              child: CircularProgressIndicator(),
            );
          }
          return Center(
            child: Text('Widget missing'),
          );
        });
  }

  Widget buildTextFormField(
      {TextEditingController controller,
      String hint,
      String label,
      String variable,
      bool enabled,
      TextInputType textInputType,
      bool obscureText = false,
      Function onChanged}) {
    return Padding(
      padding: const EdgeInsets.symmetric(vertical: 8.0),
      child: TextFormField(
        controller: controller,
        keyboardType: textInputType,
        obscureText: obscureText,
        enabled: enabled,
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
