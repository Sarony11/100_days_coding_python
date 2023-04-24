from data import question_data
from question_model import Question

question_bank = []

for i in question_data:
    question = Question(text=i["text"],answer=i["answer"])
    question_bank.append(question)

for i in question_bank:
    print(i.text)
    print(i.answer)