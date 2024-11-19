#Luis Ariza Truan
#8 de Octubre de 2024
#Entregar los divisores del número mayor que 0 que da el usuario

n1 = int(input("Escribe un número entero mayor que cero: "))
divisores = []
if n1 <= 0:
    print("El número debe ser mayor que 0")

else:
    for n in range(1, n1 +1, 1):
        if n1 % n == 0:
            divisores.append(n)

print("Los divisores de", n1, "son", divisores)

