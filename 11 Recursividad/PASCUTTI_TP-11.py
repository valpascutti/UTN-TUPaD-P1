# EJERCICIO 1
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

# EJERCICIO 2
def fibonacci(n):
    if n == 0:
        return 0 
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

# EJERCICIO 3
def potencia(base, exponente):
    if exponente == 0:
        return 1
    else:
        return base * potencia(base, exponente - 1)


def main():
    '''numero = int(input('Ingrese un numero entero positivo: '))
    for i in range(1, numero + 1):
        print(f'El factorial de {i} es {factorial(i)}')

    posicion = int(input("Ingrese una posicion para la serie de Fibonacci: "))
    print("Serie de Fibonacci: ")
    for n in range(posicion + 1):
        print(f'F({n}) = {fibonacci(n)}')'''

    base = float(input('Ingrese la base: '))
    exponente = int(input('Ingrese el exponente: '))
    resultado = potencia(base, exponente)
    print(f'{base} elevado a la {exponente} es: {resultado}')


main()