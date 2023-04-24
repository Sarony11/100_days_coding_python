import random


class User:
    def __init__(self, user_id, user_name="Paco"):
        self.id = user_id
        self.name = user_name
        self.following_n = 0
        self.following_list = []
        self.followers_n = 0
        self.followers_list = []
        
    def follow(self, user):
        user.followers_n += 1
        user.followers_list.append(self.name)
        self.following_n += 1
        self.following_list.append(user.name)

user_1 = User(user_name="Saul", user_id="00001")
user_2 = User(user_name="Maria", user_id="00002")

print(user_1.id)
print(user_1.name)

user_1.name = "Samuel"

print(user_1.name)

user_1.follow(user_2)
print(user_1.following_n,user_1.following_list)
print(user_2.followers_n,user_2.followers_list)