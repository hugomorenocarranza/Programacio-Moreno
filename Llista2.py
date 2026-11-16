llista = []
llista.append(int(input("Escriu un numero\n")))
llista.append(int(input("Escriu un segon numero\n")))
llista.append(int(input("Escriu un tercer numero\n")))
llista.append(int(input("Escriu un quart numero\n")))

print("Numeros en la llista:", llista)

llistaF =[]

while len(llista) > 0:
    if llista[0] < llista[1]:
        llistaF.append(llista[0])
        llistaF.append(llista[1])
    elif llista[0] == llista[1]:
        llistaF.append(llista[0])
        llistaF.append(llista[1])


print("Numeros ordenats:", llistaF)
