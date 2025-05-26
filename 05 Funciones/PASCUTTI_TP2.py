import math
# Ejercicio 1
def imprimir_hola_mundo():
    print("Hola Mundo!")
# Ejercicio 2
def saludar_usuario(nombre):
    print(f'Hola {nombre}')
# Ejercicio 3
def informacion_personal(nombre, apellido,edad, residencia):
    print(f'Soy {nombre} {apellido}, tengo {edad} anios y vivo en {residencia}')
# Ejercicio 4
def calcular_area_circulo(radio):
    area = math.pi * radio
    print(f'Area: {area}')

def calcular_peripetro_circulo(radio):
    perimetro = 2 * (math.pi) * radio
    print(f'Perimetro: {perimetro}')

# ejercicio 5
def segundos_a_horas(segundos):
    minutos = segundos / 60
    print(f'Son {minutos} minutos')

#Ejercicio 6
def tabla_multiplicar(numero):
    for i in range(1,11):
        print(i * numero)

# Ejercicio 7
def operaciones_basicas(a, b):
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    if b != 0:
        division = a / b
    else:
        division = None
    return(suma, resta, multiplicacion, division)

# ejercicio 8
def calcular_imc(peso, altura):
    return peso / (altura**2)

# ejercicio 9
def celsius_a_fahrenheit(celsius):
    return (celsius*9/5) + 32

def calcular_promedio(a,b,c):
    return (a+b+c)/3


def main():
    # ejercicio 1
    imprimir_hola_mundo()
    
    # ejercicio 2 y 3
    nombre = input("Ingrese su nombre: ")
    apellido = input("Ingrese su apellido: ")
    edad = int(input("Ingrese su edad: "))
    residencia = input("Ingrese su residencia: ")

    saludar_usuario(nombre)
    informacion_personal(nombre, apellido, edad, residencia)

    # ejercicio 4
    radio = float(input("Ingrese el radio del circulo: "))
    calcular_area_circulo(radio)
    calcular_peripetro_circulo(radio)
    
    # ejercicio 5
    segundos = int(input("Ingrese los segundos: "))
    segundos_a_horas(segundos)

    #ejercicio 6
    num = int(input("Ingrese un numero: "))
    tabla_multiplicar(num)
    
    # ejercicio 7
    num1 = int(input("Ingrese el primer numero: "))
    num2 = int(input("Ingrese el segundo numero: "))
    tupla = operaciones_basicas(num1, num2)
    print(f"Suma: {tupla[0]}")
    print(f"Resta: {tupla[1]}")
    print(f"Multiplicación: {tupla[2]}")
    print(f"División: {tupla[3]}")

    # ejercicio 8
    peso = float(input("Ingrese su peso (kg) : "))
    altura = float(input("Ingrese su altura (metros): "))
    imc = calcular_imc(peso, altura)
    print(f'Su imc es de {round(imc,2)}')

    # ejercicio 9
    celsius = float(input("Ingrese la temperatura en Celsius: "))
    f = celsius_a_fahrenheit(celsius)
    print(f'{celsius}°C equivalen a {round(f,2)} °F')

    # ejercicio 10
    a = float(input("Primer numero: "))
    b = float(input("Segundo numero: "))
    c = float(input("Tercer numero: "))
    promedio = calcular_promedio(a,b,c)
    print(f'Promedio: {round(promedio,2)}')

main()
