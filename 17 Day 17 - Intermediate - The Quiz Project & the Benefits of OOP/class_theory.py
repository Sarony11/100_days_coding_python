import random


class User:
    def __init__(self, user_id, user_name="Paco"):
        self.id = user_id
        self.name = user_name
        
user_1 = User(user_name="Saul",user_id=12)
             
print(user_1.name)

user_1.name = "Samuel"

print(user_1.name)