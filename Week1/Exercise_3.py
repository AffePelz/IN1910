def count_chars(word):
    d = word.lower()
    dict = {}
    for i in d:
        keys = dict.keys()
        if i in keys:
            dict[i] += 1
        else:
            dict[i] = 1
    return dict


# An exammple
example = "Hello, world!"
for char, count in count_chars(example).items():
    print(f'{char:3}{count:10}')
print("")
print("")
# Alphabetic order
for char, count in sorted(count_chars(example).items()):
    print(f'{char:3}{count:10}')
print("")
print("")
# How many times the characters appear in a sentence
for char, count in sorted(count_chars(example).items(), key=lambda item: item[1], reverse=True):
    print(f'{char:3}{count:10}')
