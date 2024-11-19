#Luis Ariza Truan
#6 de Octubre de 2024
#Saber si los números que introduce el usuario son iguales o distintos

n1 = eval(input("Escriba un número: "))
n2 = eval(input("Escruba otro número: "))
n3 = eval(input("Escriba otro número: "))

if n1 == n2 and n1 == n3:
    print("Ha escrito tres veces el mismo número")

elif n1 != n2 and n1 == n3:
    print("Ha escrito el mismo número dos veces")

else:
    print("Los tres números que ha escrito son distintos")
