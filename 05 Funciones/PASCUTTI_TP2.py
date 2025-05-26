def imprimir_hola_mundo():
    print("Hola Mundo!")

def saludar_usuario(nombre):
    print(f'Hola {nombre}')

def informacion_personal(nombre, apellido,edad, residencia):
    print(f'Soy {nombre} {apellido}, tengo {edad} anios y vivo en {residencia}')

def main():
    imprimir_hola_mundo()
    nombre = input("Ingrese su nombre: ")
    apellido = input("Ingrese su apellido: ")
    edad = int(input("Ingrese su edad: "))
    residencia = input("Ingrese su residencia: ")

    saludar_usuario(nombre)
    informacion_personal(nombre, apellido, edad, residencia)
main()
