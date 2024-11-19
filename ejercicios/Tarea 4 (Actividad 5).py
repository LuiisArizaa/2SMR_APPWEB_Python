#Luis Ariza Truan
#9 de Octubre de 2024
#Suma de todos los números enteros desde el primer número que introduce el usuario al segundo

n1 = int(input("Introduce un número entero positivo: "))
suma = 0

if n1 < 0:
    print("¡Le he pedido un número entero positivo!")

else:
    n2 = int(input(f"Introduce un número mayor que {n1}: "))

    if n2 < n1:
        print(f"¡Le he pedido un número mayor que {n1}: ")

    else:
        for n in range(n1, n2 +1, +1):
            suma = suma + n
        print("La suma desde", n1, "a", n2, "es", suma)


    

