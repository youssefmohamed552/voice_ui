from transformers import pipeline

class QA_system:
  def __init__(self):
    self.question_answering = pipeline('question-answering')

  def run(self, question, context):
    body = {
      'question': question,
      'context': context
    }

    response = self.question_answering(body)
    return response['answer']
