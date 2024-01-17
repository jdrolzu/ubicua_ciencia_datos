'''
Desarrolle un programa que permita recorrer una lista completamente, 
incluso si tiene elementos de tipo lista anidados, 
puede usar la siguiente lista como ejemplo:
lista = [1,77,"a",["hola",5,9],"pe",45,[1,2,["a","b","c"],5]]
'''

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
'''

#print('*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*')

'''
Imagina que estás creando un programa para gestionar información 
de contactos. El programa debe permitir al usuario agregar nuevos 
contactos, buscar contactos existentes, mostrar todos los contactos 
y eliminar contactos.

Cada contacto como minimo debe de tener la siguiente informacion:

    Nombre
    Numero
    Correo
'''
contact_list = {}

while True:

    print('\n*-*-*-*-*-*-*-* MENU *-*-*-*-*-*-*-*')
    print('Type 1, for adding new contact')
    print('Type 2, for searching contact')
    print('Type 3, for displaying all contacts')
    print('Type 4, for deleting a contact')
    print('Type 5, to exit\n')

    opt = input('Type one of the above options: ')

    if opt == '1':
        contact_numb = input('Type contact\'s phone number: ')
        if contact_numb in contact_list.keys():
            print('\n~~~~~ User already exists ~~~~~\n')
        else:
            contact_name = input('Type contact\'s name: ')
            contact_email = input('Type contact\'s email: ')
            contact_list[contact_numb] = {"name":contact_name, "email":contact_email}

    elif opt == '2':
        search = input('Type contact\'s phone number to search in contact list: ')
        if search in contact_list.keys():
            print('\n~~~~~ User already exists ~~~~~\n')
            print(f'Name: {contact_list[search]["name"]}')
            print(f'Phone number: {search}')
            print(f'Email: {contact_list[search]["email"]}')
        else:
            print('\n~~~~~ User does not exist ~~~~~\n')

    elif opt == '3':
        for i in contact_list.keys():
            print('\n~~~~~ Contact List ~~~~~\n')
            print(f'Name: {contact_list[i]["name"]}')
            print(f'Phone number: {i}')
            print(f'Email: {contact_list[i]["email"]}\n')

    elif opt == '4':
        delete_contact = input('Type contact\'s phone number to delete: ')
        if not delete_contact in contact_list.keys():
            print('\n~~~~~ Contact can not be deleted, it does not exist ~~~~~')
        else:
            del contact_list[delete_contact]

    elif opt == '5':
        print('Good bye')
        break
