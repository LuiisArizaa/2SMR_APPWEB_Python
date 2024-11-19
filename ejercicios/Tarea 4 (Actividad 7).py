#Luis Ariza Truan
#10 de Octubre de 2024
# pida la cantidad de números positivos que se tienen que escribir y pida números hasta que salga la cantidad de números positivos ecrita por el usuario

n1 = int(input("Escriba la cantidad de números positivos a escribir: "))

while n1 <= 0:
    print("La cantidad debe ser mayor que o.")
    n1 = int(input("Inténtalo de nuevo: "))

números = []

for n in range(n1):
    n3 = int(input("Escribe un número " + str(n + 1) + ": "))
    números.append(n3)

Positivos = []

for n3 in números:
    if n3 > 0:
        Positivos.append(n3)

print("Los números positvos introducidos son" + str(Positivos) + ": ")
