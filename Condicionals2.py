print("Escriu un número")
n1 = input()
print("Escriu un segon número")
n2 = input()
try:
    int(n1)
    int(n2)
    sN = True
except ValueError:
    sN = False
if sN:
    n1 = int(n1)
    n2 = int(n2)
    print("Escriu el número de l'operació que vols fer amb aquests números \n 1. Sumar \n 2. Restar \n 3. Multiplicar \n 4. Dividir \n 5. Elevar \n 6. Fer el módul \n 7. Divisió Entera")
    operacio = input()
    if operacio == "1":
        print(n1, " + ", n2, " = ", n1 + n2)
        canvi = input("Vols canviar l'ordre de l'operació? (s/n)\n")
        if canvi == "s":
            print(n2, " + ", n1, " = ", n2 + n1)
        elif canvi == "n":
            print("Fi del programa \n")
        else:
            print("Introdueix un parametre vàlid, (s/n)")
    elif operacio == "2":
        print(n1, " - ", n2, " = ", n1 - n2)
        canvi = input("Vols canviar l'ordre de l'operació? (s/n)\n")
        if canvi == "s":
            print(n2, " - ", n1, " = ", n2 - n1)
        elif canvi == "n":
            print("Fi del programa \n")
        else:
            print("Introdueix un parametre vàlid, (s/n)")
    elif operacio == "3":
        print(n1, " * ", n2, " = ", n1 * n2)
        canvi = input("Vols canviar l'ordre de l'operació? (s/n)\n")
        if canvi == "s":
            print(n2, " * ", n1, " = ", n2 * n1)
        elif canvi == "n":
            print("Fi del programa \n")
        else:
            print("Introdueix un parametre vàlid, (s/n)")
       
    elif operacio == "4":
        if n2 == 0:
            print("No es pot dividir entre 0")
        else: 
            print(n1, " / ", n2, " = ", n1 / n2)
            canvi = input("Vols canviar l'ordre de l'operació? (s/n)\n")
            if canvi == "s":
                print(n2, " / ", n1, " = ", n2 / n1)
            elif canvi == "n":
                print("Fi del programa \n")
            else:
                print("Introdueix un parametre vàlid, (s/n)")


    elif operacio == "5":
        print("La seva elevació és: ", int(n1) ** int(n2))
    elif operacio == "6":
        print("El seu módul és: ", int(n1) % int(n2))
    elif operacio == "7":
        print("La seva divisió entera és: ", int(n1) // int(n2))
    else:
        print("Operació no vàlida, escriu un unic número del 1 al 7 sense espais ni lletres")
    
else:
    print("Escriu un número vàlid, sense lletres ni espais")

