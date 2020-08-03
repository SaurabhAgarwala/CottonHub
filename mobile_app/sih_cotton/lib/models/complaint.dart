class Complaint {
  int id;
  String subject;
  String body;

  Complaint.fromType(Map<String, dynamic> parsedJson) {
    id = parsedJson['id'];
    subject = parsedJson['subject'];
    body = parsedJson['body'];
  }

  toJson() {
    return {
      'id': id,
      'subject': subject,
      'body': body,
    };
  }
}
