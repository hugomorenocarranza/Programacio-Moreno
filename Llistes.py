llista = [2, "Hola", 3.5]
print (llista[0])
print (llista[1])
print (llista[2])

matriu = [[1, 11, 111],[2, 22, 222]]
print (matriu[1][2])
print (matriu[0])

print (len(llista))
print (len(matriu))

llista = [2,3]+[4,6,9]
print (llista)

print (llista[1:3])

llista[2] = "gat"
print (llista)

del llista[2]
print(llista)


dni = input("Escriu el teu DNI complet sense espais\n")

numero = int(dni[0:8])
codi = ["T", "R", "W", "A", "G", "M", "Y", "F", "P", "D", "X", "B", "N", "J", "Z", "S", "Q", "V", "H", "L", "C", "K", "E"]

if(dni[8] == codi[numero % 23]):
    print("El teu DNI és correcte")
else:
    print("El teu DNI és incorrecte")




