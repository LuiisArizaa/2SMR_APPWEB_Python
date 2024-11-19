#Luis Ariza Truan
#8 de Octubre de 2024
#lista que calcule lo que hay en medio de dos valores introducidos por el usuario

n1 = int(input("Escriba un número entero: "))
n2 = int(input("Escriba otro número entero: "))

if n1 > n2:
    n1, n2 = n2, n1

print(list(range(n1 +1, n2, 1))) 
