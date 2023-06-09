class QuizzBrain():
    def __init__(self, q_bank):
        self.q_number = 0
        self.q_list = q_bank
        self.score = 0

    def next_question(self):
        q = self.q_list[self.q_number]
        self.q_number += 1
        answer = input(f"Q.{self.q_number} - {q.text} - (True/False)?: ")
        self.check_answer(q.answer,answer)

    def check_answer(self,current_answer, user_answer):
        if current_answer.lower() == user_answer.lower():
            self.score += 1
            print("Well done! Right answer")
        else:
            print("Wrong answer")
        print(f"->YOUR ACTUAL SCORE IS: {self.score}/{self.q_number}")
        print("\n")

    def final_score(self):
        print("YOU HAVE COMPLETED THE QUIZZ")
        print(f"Your final score is: {self.score}/{self.q_number}")


    def still_questions(self):
        return self.q_number+1 < len(self.q_list)