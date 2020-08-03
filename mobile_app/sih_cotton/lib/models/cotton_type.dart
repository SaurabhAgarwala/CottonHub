class CottonType {
  int id;
  String name;
  String description;

  CottonType.fromType(Map<String, dynamic> parsedJson) {
    id = parsedJson['id'];
    name = parsedJson['name'];
    description = parsedJson['description'];
  }
}
