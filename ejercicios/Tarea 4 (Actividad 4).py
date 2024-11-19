#Luis Ariza Truan
#8 de Octubre de 2024
#Que pida cuantos valores va introducir y diga cual de los valores escritos es negativos

n1 = int(input("Cuántos números vas a introducir: "))

if n1 < 0:
    print("Imposible!")

elif n1 == 0:
    print("No ha escrito ningún número negativo")

else:
    negativo = 0

    for n in range(n1):
        n2 = eval(input("Introduce un número: "))
        
        if n2 < 0:
            negativo += 1

    print("Has introducido", negativo,"números negativos")
