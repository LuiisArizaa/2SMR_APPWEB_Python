#Luis Ariza Truan
#6 de Octubre de 2024
#Calcular si un año es bisiesto o no lo es

n1 = int(input("Escribe un año y le dire si es bisiesto: "))

if n1 % 4 == 0 and n1 % 100 != 0: 
    print("El año", n1, "es un año bisiesto, porque es múltiplo de 4 sin ser múltiplo de 100.")

elif n1 % 4 != 0:
    print("El año", n1, "no es un año bisiesto.")

elif n1 % 400 == 0:
    print("El año", n1, "es un año bisiesto, porque es múltiplo de 400.")

else:
    n1 % 100 == 0 and n1 % 400 != 0
    print("El año", n1, "no es un año bisiesto, porque es múltiplo de 100 sin ser múltiplo de 400.")
    