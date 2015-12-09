inputzadas = file("input03.txt").read()
listazadas = []
x = 0
y = 0
listazadas.append((0, 0))
for i in inputzadas:
    if i == "^":
        y += 1
    elif i == "v":
        y -= 1
    elif i == "<":
        x -= 1
    elif i == ">":
        x += 1
    listazadas.append((x, y))
print len(set(listazadas))

listazadasSantaRobot = []
x = [0, 0]
y = [0, 0]
listazadasSantaRobot.append((0, 0))
for idx, i in enumerate(inputzadas):
    qual = idx % 2
    if i == "^":
        y[qual] += 1
    elif i == "v":
        y[qual] -= 1
    elif i == "<":
        x[qual] -= 1
    elif i == ">":
        x[qual] += 1
    listazadasSantaRobot.append((x[qual], y[qual]))

print len(set(listazadasSantaRobot))
