from data import list
from question import Question

score = 0
def quiz(score):
  for i in range(len(list)):
    user_answer = input(f"Q.{i}: {list[i].get_question()} T/F ? ").lower()
    if user_answer == list[i].get_answer():
      score = score + 1
      print(f"Correct. Your current score is {score}\n")
    else:
      print(f"Wrong. Your current score is {score}\n")

quiz(score)
