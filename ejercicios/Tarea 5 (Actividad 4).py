#Luis Ariza Truan
#14 de Octubre de 2024
#

def introduce_elementos_lista():
    lis = []

    n2 = int(input("¿Cuántas listas quiere escribir?: ")) 

    for n in range(n2):
        n3 = int(input("Digama cuántas palabras tiene la listas " + str(n + 1) + ": "))
        lista = []

        for i in range(n3):
            nom = eval(input("Digame la palabras " + str(i + 1) + ": "))
            lista.append(nom)
        
        lis.append(lista)
    
    print("\nLas  listas son: ")
    for i in range(len(lis)):
        print("Lista" + str(i + 1) + ": " + str(lis(i)))


introduce_elementos_lista()


    

