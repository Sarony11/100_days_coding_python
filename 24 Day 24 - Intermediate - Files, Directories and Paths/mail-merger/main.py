#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

with open("Input/Letters/starting_letter.txt", mode="r") as file:
    content = file.read()

with open("Input/Names/invited_names.txt", mode="r") as file:
    guests = list(file.readlines())
    modified_guest = [g.strip() for g in guests]

letters = [content.replace("[name]",g) for g in modified_guest]

for letter, guest in zip(letters, modified_guest):
    with open(f"Output/letter-to-{guest}.txt", mode="w") as file:
        file.write(letter)