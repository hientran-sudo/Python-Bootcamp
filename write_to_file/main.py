with open("text.txt") as file:
    contents = file.read()
    print(contents)

with open("text.txt", mode="a") as file:
    file.write("\nWhat is the weather like today?")
