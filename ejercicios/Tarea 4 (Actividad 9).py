#Luis Ariza Truan
#10 de Octubre de 2024
#Mejorar la usabilidad del programa anterior haciendo que la pregunta se repita, si el usuario no contesta S, s, N o n

n1 = int(input("Escriba un número par: "))

while n1 % 2 != 0:
    print(str(n1) + " no es número par. Intentalo de nuevo: ")
    n1 = int(input("Escriba un número par: "))

Continuar = "S"
cont = 1

while Continuar.upper() == "S" : 
    Continuar = input("¿Quiere escribir otro número par? (S/N): ")

    while Continuar.upper() not in ["S", "N"]:
        Continuar = input("¿Quiere escribir otro número par? (S/N): ")

    if Continuar.upper() == "S": 
        n1 = int(input("Escriba un número par: "))

        while n1 % 2 != 0:
            print(str(n1) + " No es número par. Inténtalo de nuevo: ")
            n1 = int(input("Escriba un número par: "))
            cont = cont +1
            
print("Ha escrito " + str(cont) + " números par." )
