name = input("Enter name: ")
name = name.capitalize()
result = len(name)

for i in range(len(name)):
    if (name[i].isspace):
        result -= 1

print(name, result)