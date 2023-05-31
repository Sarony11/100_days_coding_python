"""Define a function with unlimited arguments"""

def sumator(*args):
    suma = 0
    for n in args:
        suma += n
    print(suma)
    return

sumator(2,3,4,5,6)


"""Define a function with Many Keyworkds Arguments"""
def calculate(**kwargs):
    print(type(kwargs))
    print(kwargs) # prints a dictionary composed buy the key arguments


print(calculate(add=3, mutiply=5))


"""Define a class with keywords arguments"""

class Car():
    def __init__(self,**kw):
        # In this way, the app will return error if no maker keyword argument is provided
        self.maker = kw["maker"]
        # In this way, no error will be returned if no model keyword argument is provided
        self.model = kw.get("model")
        self.color = kw.get("color")
        self.seats = kw.get("seats")

my_car = Car(maker="Nissan", model="GT-R")
print(my_car.model)

