'''
Desarrolle un programa que permita recorrer una lista completamente, 
incluso si tiene elementos de tipo lista anidados, 
puede usar la siguiente lista como ejemplo:
lista = [1,77,"a",["hola",5,9],"pe",45,[1,2,["a","b","c"],5]]
'''

lista = [1,77,"a",["hola",5,9],"pe",45,[1,2,["a","b","c"],5]]

def sublista(elemento):
    long = len(elemento)
    i = 0
    while i < long:
        if not isinstance(elemento[i], list):
            print(elemento[i])
        else:
            sublista(elemento[i])
        i += 1

i = 0

while i < len(lista):
    if not isinstance(lista[i], list):
        print(lista[i])
    else:
        sublista(lista[i])
    i += 1



