n1 = int(input("Escriu un numero\n"))
n2 = int(input("Esciu un segon numero\n"))
suma = n1 + n2

if (n1+n2 > 10):
    print("La seva suma es més gran que 10")
else:
    print ("La seva suma es mes petita")

if(n1+n2 > 8 or n1+n2 < 4):
    print("La seva suma és més gran que 8 o més petita que 4")

if (suma > 12 and suma < 18):
    print("La seva suma és més gran que 12 i més petita que 18")

if not(suma == 13):
    print("La seva suma no és 13")
            