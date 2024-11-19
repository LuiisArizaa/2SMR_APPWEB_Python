#Luis Ariza Truan
#6 de Octubre de 2024
#El ejercicio anterior añadiendo un mensaje de error si intentan dividir por 0


n1 = eval(input("Escriba el dividiendo: "))
n2 = eval(input("Escriba el divisor: "))

if n2 == 0:
    print("No se puede dividir por 0.")

else:
    Cociente = n1 // n2
    Resto = n1 % n2

    if n1 // n2 == 0:
        print("La división es exacta: ", "Cociente: ", Cociente)
    
    else:
        print("La división no es exacta.", "Cosciente: ", Cociente,  "Resto: ", Resto,)