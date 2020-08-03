class MarketType {
  int id;
  String name;
  String description;

  MarketType.fromType(Map<String, dynamic> parsedJson) {
    id = parsedJson['id'];
    name = parsedJson['name'];
    description = parsedJson['description'];
  }
}
