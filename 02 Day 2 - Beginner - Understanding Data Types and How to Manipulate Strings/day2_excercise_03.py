""" This exercise shows:
- mathematical operation order
- how to convert string into float to make mathematical operations with inputs 
- round function 
"""
age = int(input("What is your current age? (years): "))

years_until_death = 90

years_left = years_until_death - age
months_left = years_left * 12
days_left = months_left * 30

print(f"You have {days_left} days, {months_left} months and {years_left} years left.")
