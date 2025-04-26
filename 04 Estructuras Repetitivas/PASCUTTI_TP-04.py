# EJERCICIO 1

for i in range(1, 101):
    print(i)


# EJERCICIO 2

numero = int(input("Ingrese un numero entero: "))
contador = 0
numero = str(numero)

for i in range(len(numero)):
    contador += 1

print(f"Tiene {contador} digitos")


# EJERCICIO 3

nro1 = int(input("Ingrese un numero: "))
nro2 = int(input("Ingrese un numero mayor al anterior: "))
acumulador = 0
if nro1 < nro2:
    for i in range(nro1 + 1, nro2):
        acumulador += i

    print(f"La suma de los nros entre el rango es: {acumulador}")
else:
    print("Error! El primer numero debe ser mayor que el segundo")


# EJERCICIO 4

numero = int(input("Ingrese un numero (ingresa un 0 para detenerte): "))
acumulador = 0

while numero != 0:
    acumulador += numero
    numero = int(input("Ingrese otro numero: ")) 

print(f"La suma de los numeros ingresados es {acumulador}")


# EJERCICIO 5
import random
numero = random.randint(0, 9)
contador = 0 


num_user = int(input("Adivine el numero entre el 0 al 9: "))
contador += 1
while num_user != numero:
    num_user = int(input("Ingrese otro numero: "))
    contador += 1

print(f'Necesitaste de {contador} intentos para adivinar el numero :)')



# EJERCICIO 6

for i in range(100, -1, -1):
    if i % 2 == 0:
        print(i)


# EJERCICIO 7

nro = int(input("Ingrese un numero entero: "))
acu = 0

for i in range(0, nro + 1):
    acu += i
print(f'La suma de todos los numeros comprendidos entre 0 y {nro} es: {acu}')


# EJERCICIO 8
negativos = 0
positivos = 0
pares = 0 
impares = 0

for i in range(5):
    number = int(input("Ingrese un numero: "))
    if number % 2 == 0:
        pares += 1
    else:
        impares += 1
    if number > 0:
        positivos += 1
    else: 
        negativos += 1

print(f"Cantidad de números pares: {pares}")
print(f"Cantidad de números impares: {impares}")
print(f"Cantidad de números positivos: {positivos}")
print(f"Cantidad de números negativos: {negativos}")


# EJERCICIO 9

suma = 0
for i in range(100):
    numero = int(input("Ingrese un numero entero: "))
    suma += numero

media = suma / 100
print(f'La media de los numeros ingresados es: {media}')


# EJERCICIO 10
numero = input("Ingrese un número: ")

if numero[0] == '-':  
    invertido = '-' + numero[:0:-1]  
else:
    invertido = numero[::-1]  

print(f"El número invertido es: {invertido}")