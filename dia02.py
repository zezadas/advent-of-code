inputzadas = file("input02.txt").read()
papel = 0
for i in inputzadas.split("\n"):
    a = list()
    caixa = [int(j) for j in i.split("x")]
    l = caixa[0]
    w = caixa[1]
    h = caixa[2]
    a.append(l * w)
    a.append(w * h)
    a.append(h * l)
    minzadas = min(a)
    papel += 2 * a[0] + 2 * a[1] + 2 * a[2] + minzadas

print papel

fita = 0
for i in inputzadas.split("\n"):
    a = list()
    caixa = [int(j) for j in i.split("x")]
    l = caixa[0]
    w = caixa[1]
    h = caixa[2]
    min1 = min(caixa)
    caixa.remove(min1)
    min2 = min(caixa)
    fita += 2 * min1 + 2 * min2 + l * w * h

print fita
