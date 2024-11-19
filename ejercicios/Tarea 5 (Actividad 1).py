#Luis Ariza Truan
#12 de Octubre de 2024
#Dibujar un rectángulo segun la altura y anchura que diga el usuario


def dibujar(n2, n1):
    for i in range(n2):
        print("*" * n1)

n1 = int(input("Anchura del Rectángulo: "))
n2 = int(input("Altura del rectángulo: "))

if n2 > 0 and n1 > 0:
    dibujar(n2, n1)

else:
    print("La altura y la anchura deben ser números positivos")
