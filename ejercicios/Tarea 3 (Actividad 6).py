#Luis Ariza Truan
#6 de Octubre de 2024
#Pedir dos números al usuario y diga si el mayor de los dos números es múltiplo del otro

n1 = int(input("Escriba un número entero: "))
n2 = int(input("Escriba otro número entero: "))

if n1 < 0 or n2 < 0:
    print("Lo siento, este programa no admite números negativos")

elif n1 == 0 or n2 == 0:
    print("Lo siento, este programa no admite valores nulos")

elif n1 > n2:
    if n1 % n2 == 0: 
        print(n1, "es múltiplo de", n2)

    else: 
        n1 % n2 != 0
        print(n1, "no es múltiplo de", n2)

elif n1 < n2:
    if n2 % n1 == 0:
        print(n2, "es múltiplo de", n1)

    else:
        n2 % n1 != 0
        print(n2, "no es múltiplo de", n1)

else: 
    if n1 == n2:
        n1 % n2 == 0
        print(n1, "es múltiplo de", n2)
    
    else:
        n1 % n2 != 0
        print(n1, "no es múltiplo de", n2)
