class User {
  int id;
  String firstName;
  String lastName;
  String email;
  String username;
  String address;
  String pan;
  String aadhar;
  String gst;
  int typeOfUser;

  User.fromType(Map<String, dynamic> parsedJson) {
    id = parsedJson['id'];
    firstName = parsedJson['first_name'];
    lastName = parsedJson['last_name'];
    email = parsedJson['email'];
    username = parsedJson['username'];
    address = parsedJson['address'];
    pan = parsedJson['pan'];
    aadhar = parsedJson['aadhar'];
    gst = parsedJson['gst'];
    typeOfUser = parsedJson['type_of_user'];
  }
}
