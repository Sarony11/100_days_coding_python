student_dict = {
    "student": ["Angela", "James", "Lily"], 
    "score": [56, 76, 98]
}

#Looping through dictionaries:
for (key, value) in student_dict.items():
    #Access key and value
    pass

import pandas
student_data_frame = pandas.DataFrame(student_dict)

#Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    #Access index and row
    #Access row.student or row.score
    pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

#TODO 1. Create a dictionary in this format:
{"A": "Alfa", "B": "Bravo"}
NATO_df = pandas.read_csv("nato_phonetic_alphabet.csv")
print(NATO_df)

NATO_dict = {letter: code for letter,code in zip(NATO_df.letter,NATO_df.code)}
print(NATO_dict)

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
word = input("Give me a word: ").upper()
word_code = [NATO_dict[l] for l in word]
print(word_code)

