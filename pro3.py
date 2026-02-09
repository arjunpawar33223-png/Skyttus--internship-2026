f = open("data.txt", "r")
text = f.read().lower()
words = text.split()

word_count = {}
for w in words:
    word_count[w] = word_count.get(w, 0) + 1

print(word_count)
f.close()