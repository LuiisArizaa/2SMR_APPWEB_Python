#Luis Ariza Truan
#13 de Octubre de 2024
#El usuario introduce dos años y el programa escriba cuántos años bisiestos hay entre esas dos fechas.


def año_bisiesto(n):
    return(n % 4 == 0 and n % 100 != 0) or (n % 400 == 0)

n1 = int(input("Escriba un año: "))
n2 = int(input("Escriba otro año posterior a " + str(n1) + ": "))

if n2 < n1:
    print(n2, "no es nayor que", n1)
    input(int(("Inténtalo de nuevo: ")))

else:
    if n1 > n2:
        n1, n2 = n2, n1

    bisiestos = 0
    for n in range(n1, n2 + 1):
        if año_bisiesto(n):
            bisiestos = bisiestos + 1
    
    print("Hay", bisiestos, "años bisiestos entre", n1, "y", n2)



