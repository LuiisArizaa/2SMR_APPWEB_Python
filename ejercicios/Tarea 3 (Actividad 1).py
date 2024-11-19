#Luis Ariza Truan
#6 de octubre de 2024
#Saber si es correcto el número par o impar

n1 = input("Escribe un número par: ")
n2 = input("Escribe un número inpar: ")
n1 = eval(n1)
n2 = eval(n2)

if n1 % 2 == 0 and n2 % 2 != 0:
    print("Gracias por su colaboración!")

else:
    print("Uno de los valores es incorrecto")

