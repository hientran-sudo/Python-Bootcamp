#PLACEHOLDER = "[name]"

with open("./Input/Names/invited_name.txt") as file:
    lines = file.readlines()

for line in lines:
    new_line = line.strip()
    f = open(f"./Output/ReadyToSend/letter_to_{new_line}.txt","w")

    with open("./Input/Letters/starting_letter.txt") as file1:
        data = file1.read()
        f.write(data) 
    
    #with open(f"./Output/ReadyToSend/letter_to_{new_line}.txt","r") as f1:
        #edit = f1.read()
        #edit = edit.replace(PLACEHOLDER,new_line)
   
    #with open(f"./Output/ReadyToSend/letter_to_{new_line}.txt", mode="a") as f1:
        #f1.write(edit)
