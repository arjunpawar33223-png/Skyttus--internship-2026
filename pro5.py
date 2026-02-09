items = ["Apple", "Banana", "Mango"]

f = open("data.txt", "a")
for item in items:
    f.write(item + "\n")
f.close()