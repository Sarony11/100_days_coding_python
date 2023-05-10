"""
Create a dict called result.
Result will take each word in a sentence and will calculate the letters in each word
DO NOT create the dictionary direcly. Use Dict comprehension.
"""

sentence = input("Give me your sentence: ").split()
print(sentence)
result = {word: len(word) for word in sentence}
print(result)