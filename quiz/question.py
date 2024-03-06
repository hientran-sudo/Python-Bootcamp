class Question:
  def __init__(self, question, answer):
    self.quest = question
    self.ans = answer

  def get_question(self):
    return self.quest

  def get_answer(self):
    return self.ans
