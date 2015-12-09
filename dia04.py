inputzadas = file("input04.txt").read()
import hashlib


def gerador(textozadas):
    i=0
    while True:
        i+=1
        yield (hashlib.md5(textozadas+str(i)).hexdigest(),i)

for j in gerador(inputzadas):
    if j[0][:5] == "00000":
        print j[1]
        break

for j in gerador(inputzadas):
    if j[0][:6] == "000000":
        print j[1]
        break
