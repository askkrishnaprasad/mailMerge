#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

with open("./Input/Letters/starting_letter.txt") as ref_letter:
    letter_content = ref_letter.read()

with open("./Input/Names/invited_names.txt") as name_list_file:
    names_list = name_list_file.readlines()

for name in names_list:
    with open(f"./Output/ReadyToSend/{name}.text", mode="w") as output_file:
        name = name.rstrip()
        new_content = letter_content.replace("[name]", name)
        output_file.write(new_content)

