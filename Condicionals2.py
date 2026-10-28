print("Escriu un número")
n1 = input()
print("Escriu un segon número")
n2 = input()

print("Escriu el número de l'operació que vols fer amb aquests números \n 1. Sumar \n 2. Restar \n 3. Multiplicar \n 4. Dividir \n 5. Elevar \n 6. Fer el módul \n 7. Divisió Entera")
operacio = input()
if operacio
if operacio == "1":
    print("La seva suma és: ", int(n1) + int(n2))
elif operacio == "2":
    print("La seva resta és: ", int(n1) - int(n2))
elif operacio == "3":
    print("La seva multiplicació és: ", int(n1) * int(n2))
elif operacio == "4":
    print("La seva divisió és: ", int(n1) / int(n2))
elif operacio == "5":
    print("La seva elevació és: ", int(n1) ** int(n2))
elif operacio == "6":
    print("El seu módul és: ", int(n1) % int(n2))
elif operacio == "7":
    print("La seva divisió entera és: ", int(n1) // int(n2))
else:
    print("Operació no vàlida, escriu un unic número del 1 al 7 sense espais ni lletres")
