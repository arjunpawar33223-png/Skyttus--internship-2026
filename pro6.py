word = input("Enter word to search: ")

f = open("data.txt", "r")
for line in f:
    if word in line:
        print(line.strip())
f.close()