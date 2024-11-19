#Luis Ariza Truan
# 6 de Octubre de 2024
#Pedir número par y si es correcto que pida el impar, sino que de un mensaje de error

n1 = input("Escribe un número par: ")
n1 = eval(n1)

if n1 % 2 == 0:
    n2 = eval(input("Escribe un número inpar: "))
    if n2 % 2 != 0:
        print("Gracias por su colaboración!")
    else:
        print("No ha escrito un número impar")

else:
    print("No ha escrito un número par")