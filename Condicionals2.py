def cambiarOrdre(n1,n2):
    print("Vols cambiar l'ordre de l'operació de (", n1, ", ", n2, ") a: (", n2, ", ", n1, ")? (si/no)")
    resposta = input()
    if resposta == "si":
        return n2, n1
    elif resposta == "no":
        print("No s'ha canviat l'ordre dels números")
        return n1, n2
    else:
        print("Resposta no vàlida, escriu 'si' o 'no' en minuscules")
        return n1, n2
print("Escriu un número")
n1 = input()
print("Escriu un segon número")
n2 = input()
if n1.isnumeric() and n2.isnumeric():
    print("Escriu el número de l'operació que vols fer amb aquests números \n 1. Sumar \n 2. Restar \n 3. Multiplicar \n 4. Dividir \n 5. Elevar \n 6. Fer el módul \n 7. Divisió Entera")
    operacio = input()
    if operacio == "1":
        n1, n2 = cambiarOrdre(n1, n2)
        print("La seva suma és: ", int(n1) + int(n2))
    elif operacio == "2":
        n1, n2 = cambiarOrdre(n1, n2)
        print("La seva resta és: ", int(n1) - int(n2))
    elif operacio == "3":
        n1, n2 = cambiarOrdre(n1, n2)
        print("La seva multiplicació és: ", int(n1) * int(n2))
    elif operacio == "4":
        n1, n2 = cambiarOrdre(n1, n2)
        print("La seva divisió és: ", int(n1) / int(n2))
    elif operacio == "5":
        n1, n2 = cambiarOrdre(n1, n2)
        print("La seva elevació és: ", int(n1) ** int(n2))
    elif operacio == "6":
        n1, n2 = cambiarOrdre(n1, n2)
        print("El seu módul és: ", int(n1) % int(n2))
    elif operacio == "7":
        n1, n2 = cambiarOrdre(n1, n2)
        print("La seva divisió entera és: ", int(n1) // int(n2))
    else:
        print("Operació no vàlida, escriu un unic número del 1 al 7 sense espais ni lletres")
    
else:
    print("Escriu un número vàlid, sense lletres ni espais")

