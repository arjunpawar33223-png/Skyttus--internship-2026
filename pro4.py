f = open("sentences.txt", "w")
for i in range(5):
    s = input("Enter sentence: ")
    f.write(s + "\n")
f.close()