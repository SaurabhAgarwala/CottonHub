class Faq {
  int id;
  String question;
  String answer;

  Faq.fromType(Map<String, dynamic> parsedJson) {
    id = parsedJson['id'];
    question = parsedJson['question'];
    answer = parsedJson['answer'];
  }
}
