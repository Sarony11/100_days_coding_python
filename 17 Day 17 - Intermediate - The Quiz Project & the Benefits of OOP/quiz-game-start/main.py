from data import question_data
from question_model import Question
from quiz_brain import QuizzBrain

question_bank = []

for i in question_data:
    question = Question(text=i["text"],answer=i["answer"])
    question_bank.append(question)

quizz = QuizzBrain(question_bank)

while quizz.still_questions():
    quizz.next_question()
quizz.final_score()