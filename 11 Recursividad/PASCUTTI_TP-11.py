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

# EJERCICIO 4
def decimal_a_binario(n):
    if n == 0:
        return ""
    else:
        return decimal_a_binario(n // 2) + str(n % 2)

# ejercicio 5
def es_palindromo(palabra):
    if len(palabra) <= 1:
        return True
    if palabra[0] != palabra[-1]:
        return False
    return es_palindromo(palabra[1:-1])

# EJERCICIO 6
def suma_digitos(n):
    if n < 10:
        return n
    else:
        return n % 10 + suma_digitos(n // 10)

def main():
    '''numero = int(input('Ingrese un numero entero positivo: '))
    for i in range(1, numero + 1):
        print(f'El factorial de {i} es {factorial(i)}')

    posicion = int(input("Ingrese una posicion para la serie de Fibonacci: "))
    print("Serie de Fibonacci: ")
    for n in range(posicion + 1):
        print(f'F({n}) = {fibonacci(n)}')

    base = float(input('Ingrese la base: '))
    exponente = int(input('Ingrese el exponente: '))
    resultado = potencia(base, exponente)
    print(f'{base} elevado a la {exponente} es: {resultado}')

    num = int(input("Ingrese un numero entero positivo: "))
    if num == 0:
        print("El numero binario es: 0")
    else:
        binario = decimal_a_binario(num)
        print(f'El numero binario es: {binario}')

    palid = input("ingrese palabra: ")
    palabra_pal = es_palindromo(palid)
    if palabra_pal:
        print("Es palindromo")
    else: 
        print("No es")'''

    sum_num = int(input("Numero: "))
    suma = suma_digitos(sum_num)
    print(suma)
main()