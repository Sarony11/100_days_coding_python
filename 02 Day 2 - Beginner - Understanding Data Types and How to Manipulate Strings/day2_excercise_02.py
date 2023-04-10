""" This exercise shows:
- mathematical operation order
- how to convert string into float to make mathematical operations with inputs 
- round function 
"""

weight = input("What is your weight in kilograms?: ")
height = input("What is your weight in meters? ")

weight_in_kg = float(weight)
height_in_m = float(height)

bmi = weight_in_kg / height_in_m ** 2

print("Your BMI factor is: ", round(bmi, 2))