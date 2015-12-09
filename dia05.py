inputzadas = file("input05.txt").read()
disallowed = ["ab", "cd", "pq", "xy"]


def not_naughty(word):
    for dis in disallowed:
        if dis in word:
            return 0
    a = word.count("a") + word.count("e") + word.count("i") + word.count("o") + word.count("u")
    if a < 3:
        return 0
    for i in range(len(word) - 1):
        if word[i] == word[i + 1]:
            return 1
    return 0


counter = 0
for word in inputzadas.split("\n"):
    counter += not_naughty(word)
print counter


def not_naughty2(word):
    um = False
    dois = False
    for i in range(len(word) - 1):
        if word.count(word[i:i + 2]) > 1:
            um = True
        if i<len (word)-2 and word[i] == word[i + 2]:
            dois = True
    if um and dois:
        return 1
    return 0

counter = 0
for word in inputzadas.split("\n"):
    counter += not_naughty2(word)
print counter
