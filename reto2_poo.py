'''
En un taller de reparación de vehículos, se necesita diseñar un sistema para llevar un registro de las reparaciones realizadas. 
Existen dos tipos principales de vehículos: automóviles y motocicletas.
Cada tipo de vehículo tiene diferentes componentes y tipos de reparaciones asociados.

Los vehículos tendrán las siguientes características:

Atributos:

    marca: La marca del vehículo.
    modelo: El modelo del vehículo.

Respecto a los comportamientos, deberían de tener un método que permita obtener la información del vehículo junto a su respectivo constructor


La clase Automóvil debe tener un atributo adicional:

    puertas: Número de puertas del automóvil.

La clase Motocicleta debe tener un atributo adicional:

    cilindraje: El cilindraje de la motocicleta.

Tanto Automóvil como Motocicleta deben tener su respectivo método para mostrar la información del vehículo incluyendo estos nuevos atributos.

En el taller también debe haber un método para poder calcular el costo de una reparación con las siguientes indicaciones:

Si el daño es "motor":

    150000 para automóviles
    100000 para motocicletas

Si el daño es "sistema eléctrico"

    75000 automoviles
    50000 motocicletas

Si el daño es "frenos":

    80000 para los 2

Si el daño es "suspensión":

    60000 y solo se realizará esta reparación a motocicletas
'''

class Vehiculos:
    def __init__(self, tipo, marca, modelo):
        self.tipo = tipo
        self.marca = marca
        self.modelo = modelo


'''
Crear un programa en Python que permita a los usuarios convertir temperaturas entre tres escalas comunes: 
Celsius (°C), Fahrenheit (°F) y Kelvin (K). 
El programa debe ser interactivo y permitir al usuario seleccionar que tipo de conversion desea realizar, 
ingresando el valor de temperatura y obteniendo la conversión.

Instrucciones

    El programa debe mostrar un menú interactivo que permita al usuario seleccionar que conversion quiere realizar (C a F, F a K, K a C).
    El usuario debe ingresar la temperatura en la escala de entrada.
    El programa debe realizar la conversión de temperatura y mostrar el resultado en la escala de salida.

'''

def menu():
    print('Para convertir de C a F, presione: 1')
    print('Para convertir de C a K, presione: 2')
    print('Para convertir de F a C, presione: 3')
    print('Para convertir de F a K, presione: 4')
    print('Para convertir de K a C, presione: 5')
    print('Para convertir de K a F, presione: 6')
    print('Para terminar, presione: 7\n')

def c_to_f():
    temp_c = float(input('Ingrese temperatura en Celsius: '))
    temp_f = round((temp_c * (9/5) + 32), 1)
    print(f'{temp_c} celsius equivalen a {temp_f} farenheit.')

def c_to_k():
    temp_c = float(input('Ingrese temperatura en Celsius: '))
    temp_k = round((temp_c + 273.15), 1)
    print(f'{temp_c} celsius equivalen a {temp_k} kelvin.')

def f_to_c():
    temp_f = float(input('Ingrese temperatura en Farenheit: '))
    temp_c = round(((temp_f - 32) * (5/9)), 1)
    print(f'{temp_f} farenheit equivalen a {temp_c} celsius.')

def f_to_k():
    temp_f = float(input('Ingrese temperatura en Farenheit: '))
    temp_k = round(((temp_f - 32) * (5/9) + 273.15), 1)
    print(f'{temp_f} farenheit equivalen a {temp_k} kelvin.')

def k_to_c():
    temp_k = float(input('Ingrese temperatura en Kelvin: '))
    temp_c = round((temp_k - 273.15), 1)
    print(f'{temp_k} kelvin equivalen a {temp_c} celsius.')

def k_to_f():
    temp_k = float(input('Ingrese temperatura en Kelvin: '))
    temp_f = round(((temp_k - 273.15) * (9/5) + 32), 1)
    print(f'{temp_k} kelvin equivalen a {temp_f} farenheit.')

while True:
    print('\n***** Conversor de Temperaturas *****')
    menu()
    user_option = input('Ingrese la opción deseada: ')
    if user_option == '1':
        c_to_f()
    elif user_option == '2':
        c_to_k()
    elif user_option == '3':
        f_to_c()
    elif user_option == '4':
        f_to_k()
    elif user_option == '5':
        k_to_c()
    elif user_option == '6':
        k_to_f()
    elif user_option == '7':
        break
    else:
        print('Opción no válida.')


