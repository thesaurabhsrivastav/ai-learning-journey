file = open("example.txt", "r")

content = file.read()

print(content)

file.close()

#This is more better way
with open("example.txt", "r") as file:
    content = file.read()
    print(content)

with open("notes.txt", "w") as file:
    file.write("Hello AI")

with open("notes.txt", "a") as file:
    file.write("\nNew line added")

#Read Line by Line
with open("example.txt", "r") as file:

    for line in file:
        print(line)