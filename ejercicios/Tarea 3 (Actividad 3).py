#Luis Ariza Truan
#6 de Octubre de 2024
#Calcular una división y decir si es entera o no

n1 = eval(input("Escriba el dividiendo: "))
n2 = eval(input("Escriba el divisor: "))

Cociente = n1 // n2
Resto = n1 % n2

if n1 // n2 == 0:
    div = Cociente
    print("La división es exacta: ", "Cociente: ")
 
else:
    res = Resto
    div = Cociente
    print("La división no es exacta.", "Cosciente: ", div,  "Resto: ", res,)
