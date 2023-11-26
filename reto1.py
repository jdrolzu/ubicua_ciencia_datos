#Para tributar un determinado impuesto se debe ser mayor de 16 años y tener unos ingresos iguales o superiores a 1000 € mensuales.
#Desarrolle un programa que pregunte al usuario su edad y sus ingresos mensuales y muestre por pantalla si el usuario tiene que tributar o no.

min_age = 16
income = 1000

try: 
    user_age = int(input('Digite la edad: '))
    user_income = float(input('Digite los ingresos mensuales: '))

    if user_age > min_age and user_income >= income:
        print(f'El usuario con: {user_age} años e ingresos mensuales iguales o superiores a: ${user_income}, DEBE tributar')
    else:
        print('El usuario NO DEBE tributar')

except:
    print('Error en el ingreso de datos')