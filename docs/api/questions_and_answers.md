# Questions And Answers

## Retrieving Questions and Answers

**Request**:

`GET` `questions_and_answers/`

Parameters:

Name       | Type   | Required | Description
-----------|--------|----------|------------
student_id | integer | No      | The Student id

**Response**:
```json
[{
    "question": "Conforme visto na imagem acima, a questão 01 é uma...",
    "answered_alternative": "Alternativa 01",
    "is_correct": false
},
  {
    "question": "Conforme visto na imagem acima, a questão 02 é uma...",
    "answered_alternative": "Alternativa 02",
    "is_correct": true
}]
```
