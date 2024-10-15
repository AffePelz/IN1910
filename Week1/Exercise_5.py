infile = open("names.txt", "r")

for line in infile:
    words = line.split(",")
    words.sort()


def value(word):
    count = 0
    alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    for i in range(0, len(word)):
        for j in range(0, 26):
            if word[i] == alphabet[j]:
                count += (j+1)
    return count


total = 0
for i in range(0, len(words)):
    total += (words.index(words[i]) + 1)*value(words[i])

print(total)
