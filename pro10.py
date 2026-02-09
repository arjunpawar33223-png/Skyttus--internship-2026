with open("data.txt", "r") as f:
    content = f.read()

with open("backup.txt", "w") as f:
    f.write(content)

print("Backup created")