#Luis Ariza Truan
#10 de Octubre de 2024
#Sacar el número mayor, menor y media aritmética de los valores introducidos por el usuario

n1 = int(input("¿Cuántos valores va introducir?: "))

if n1 < 0:
    print("¡Imposible!")

else:
    números = []

    for n in range(n1):
        n2 = int(input("Introduzca el número" + str(n + 1) + ": "))
        números.append(n2)
    
    mayor = números[0]
    menor = números[0]
    suma = 0


    for n2 in números:
        if n2 > mayor:
            mayor = n2
        
        else:
            n2 < menor
            menor = n2
        suma += n2
    
    media = suma / n1

    print("El números más pequeño introducido es:" + str(menor))
    print("El número más grande introducido es:" + str(mayor))
    print("La media de los números introducidos es: " + str(media))