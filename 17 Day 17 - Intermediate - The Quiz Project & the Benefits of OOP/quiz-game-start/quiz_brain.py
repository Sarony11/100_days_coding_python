class QuizzBrain():
    def __init__(self, q_bank):
        self.q_number = 0
        self.q_list = q_bank

    def next_question(self):
        q = self.q_list[self.q_number]
        self.q_number += 1
        a = input(f"Q.{self.q_number} - {q.text} - (True/False)?: ")
        return a

    def still_questions(self):
        return self.q_number+1 < len(self.q_list)