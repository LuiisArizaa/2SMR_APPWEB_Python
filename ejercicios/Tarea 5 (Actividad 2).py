#Luis Ariza Truan
#13 de Octubre de 2024
#Dibujar un triángulo sabiendo la anchura de el (introducido por el usuario)

n1 = int(input("Anchura del triángulo: "))

def dibujar_triángulo(n1):
    for n in range(1, n1+ 1):
        línea = "*" * n
        print(línea)
    
    for i in range(n1 - 1, 0, -1):
        línea = "*" * i
        print(línea)

if n1 < 0:
    print("La anchura debe ser positivo")

else:
    dibujar_triángulo(n1)