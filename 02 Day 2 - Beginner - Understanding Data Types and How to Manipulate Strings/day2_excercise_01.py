"""
This excercise shows:
- How strings can be split into digits/characters
- How to convert string characters into numerical digits
- How to operate with int digits (impossible with string characters)
"""

number = input("Type a number: ")
sum_numbers = 0
for position in number:
    sum_numbers += int(position)

print(sum_numbers)