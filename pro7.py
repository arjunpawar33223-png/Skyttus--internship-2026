old = input("Enter old word: ")
new = input("Enter new word: ")

with open("data.txt", "r") as f:
    content = f.read()

content = content.replace(old, new)

with open("data.txt", "w") as f:
    f.write(content)

print("Word replaced successfully")