class Animal:
    def __init__(self):
        self.num_eyes = 2
    
    def breathe(self):
        print("Breathe")
    
class Fish(Animal):
    def __init__(self):
        super().__init__()

    def swim(self):
        print("Swim")

    def breathe(self):
        super().breathe()
        print("Breathe under water")

nemo = Fish()
nemo.swim()
print(nemo.num_eyes)
nemo.breathe()