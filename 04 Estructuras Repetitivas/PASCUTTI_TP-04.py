# EJERCICIO 1
'''
for i in range(1, 101):
    print(i)
'''

# EJERCICIO 2

numero = int(input("Ingrese un numero entero: "))
contador = 0
numero = str(numero)

for i in range(len(numero)):
    contador += 1

print(f"Tiene {contador} digitos")