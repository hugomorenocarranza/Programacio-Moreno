llistaNoms = []
for i in range(3):
    llistaNoms.append(input("Introdueix un nom:"))
print (llistaNoms)

for i in range(17,101):
    if (i%2 == 0):
        print (i, end=" ")

notes = [[6,6,7,10,9],[10,7,6,7,7],[5,5,10,7,10]]
n = 0
posicion = []
for i in notes:
    for j in i:
        if j == 10:
            n += 1
            posiciones.append((notes.index(i), i.index(j)))
