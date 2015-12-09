inputzadas = file("input01.txt").read()
sobe = inputzadas.count('(')
desce = inputzadas.count(')')
print sobe - desce

a = 0
for i, val in enumerate(inputzadas):
    a += 1 if val == "(" else -1
    if a == -1:
        print i+1
        break
