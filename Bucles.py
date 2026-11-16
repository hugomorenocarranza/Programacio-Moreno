llistaNoms = []
for i in range(3):
    llistaNoms.append(input("Introdueix un nom:"))
print (llistaNoms)

for i in range(17,101):
    if (i%2 == 0):
        print (i, end=" ")

print ("")

notes = [[6,6,7,10,9],[10,7,6,7,7],[5,5,10,7,10]]
n = 0
posicion = []
for i in notes:
    for j in i:
        if j == 10:
            n += 1
            posicion.append((notes.index(i), i.index(j)))

print ("Hi ha", n, "deus en total")
print (f"Els deus estan a les posicions:\n Fila: {posicion[0][0]} Columna: {posicion[0][1]}\n Fila: {posicion[1][0]} Columna: {posicion[1][1]}\n Fila: {posicion[2][0]} Columna: {posicion[2][1]}\n Fila: {posicion[3][0]} Columna: {posicion[3][1]}\n")

secret = 5
while int(input("Introdueix un número entre 1 i 10: ")) != secret:
    print ("Número incorrecte, torna-ho a provar")
print("Correcte!")