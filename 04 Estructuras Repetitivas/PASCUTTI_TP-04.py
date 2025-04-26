# EJERCICIO 1
'''
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
'''
