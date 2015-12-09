inputzadas = file("input06.txt").read()
arrayzadas = [[0 for x in range(1000)] for x in range(1000)]


def processar_linha(linha):
    d = linha.split(' ')
    if len(d) == 5:
        if d[1] == "on":
            a = 1
        elif d[1] == "off":
            a = -1
        else:
            print "fudeu1"
    elif len(d) == 4:
        a = 0
    else:
        print "fudeu2"
    (x1, y1) = d[-3].split(',')
    (x2, y2) = d[-1].split(',')
    return (a, int(x1), int(y1), int(x2), int(y2))


def switchzadas(a, conteudo):
    if (a == 0):
        return int(conteudo != 1)
    return 1 if a == 1 else 0


for linha in inputzadas.split('\n'):
    (a, x1, y1, x2, y2) = processar_linha(linha)
    for i in range(x1, x2 + 1):
        for j in range(y1, y2 + 1):
            arrayzadas[i][j] = switchzadas(a, arrayzadas[i][j])

print sum(x.count(1) for x in arrayzadas)


def switchzadas2(a):
    if a == 0:
        return 2
    return a

arrayzadas = [[0 for x in range(1000)] for x in range(1000)]
for linha in inputzadas.split('\n'):
    (a, x1, y1, x2, y2) = processar_linha(linha)
    for i in range(x1, x2 + 1):
        for j in range(y1, y2 + 1):
            arrayzadas[i][j] += [switchzadas2(a),0][arrayzadas[i][j]+switchzadas2(a)<0]

print sum(sum(x) for x in arrayzadas)
