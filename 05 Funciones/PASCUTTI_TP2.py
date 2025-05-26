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

def main():
    # ejercicio 1
    '''imprimir_hola_mundo()
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
    segundos_a_horas(segundos)'''

    #ejercicio 6
    num = int(input("Ingrese un numero: "))
    tabla_multiplicar(num)
main()
