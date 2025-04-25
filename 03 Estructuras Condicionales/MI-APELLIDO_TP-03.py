# ejercicio 1
'''edad = int(input("Ingrese su edad:"))

if edad > 18:
    print("Es mayor de edad")

# ejercicio 2
nota = int(input("Ingrese su nota: "))
if nota >= 6:
    print("Aprobado")
else:
    print("Desaprobado")
#ejercicio 3
numero = int(input("Ingrese un numero: "))

if numero % 2 == 0:
    print("Ha ingresado un numero par")
else:
    print("Por favor, ingrese un numero par")

#ejercicio 4
edad = int(input("Ingrese su edad: "))

if edad < 12:
    print("Ninio/a")
elif edad >= 12 and edad <18:
    print("Adolescente")
elif edad >= 18 and edad <30:
    print("Adulto/a joven")
else:
    print("Adulto/a")

#ejercicio 5
password = str(input('Ingrese una contrasenia de entre 8 y 14 caracteres: '))
if len(password) >= 8 and len(password) <= 14:
    print("Ha ingresado una contrasenia correcta")
else:
    print("Por favor, ingrese una contrasenia de entre 8 y 14 caracteres")

#ejercicio 6
import random
from statistics import mean, median, mode

numeros_aleatorios = [random.randint(1,100) for i in range(50)]

media = mean(numeros_aleatorios)
mediana = median(numeros_aleatorios)
moda = mode(numeros_aleatorios)

print("Numeros aleatorios: ", numeros_aleatorios)
print("MEDIA: ", media)
print("MEDIANA: ", mediana)
print("MODA: ", moda)

if media > mediana and mediana > moda:
    print("Hay sesgo positivo o a la derecha")
elif media < mediana and mediana < moda:
    print("Hay sesgo negativo o a la izquierda")
else:
    print("No hay sesgo")


#Ejercicio 7
frase = input("Ingrese una frase o palabra: ").lower()

if frase[-1] in "aeiou":
    print(frase,"!")
else:
    print(frase)

#Ejercicio 8
nombre = input("Ingrese su nombre: ")
print("***MENU OPCIONES***")
print("Nombre en mayusculas")
print("Nombre en minusculas")
print("Nombre con la primera letra en mayuscula")

opc = int(input("Seleccione una opcion: "))

if opc == 1:
    print(nombre.upper())
elif opc == 2:
    print(nombre.lower())
elif opc == 3:
    print(nombre.title())
else:
    print("ERROR! ingrese una opcion valida")
'''

#ejercicio 9

