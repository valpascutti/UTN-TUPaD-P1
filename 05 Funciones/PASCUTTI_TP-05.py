# EJERICIO 1
'''
lista_mult4 = []

for i in range(1, 101):
    if i % 4 == 0:
        lista_mult4.append(i)
    
print(lista_mult4)


# EJERCICIO 2

comida = ["Hamburguese", "Lomito", "Pizza", "Asado", "Tarta"]

ult_ubicacion = comida[-2]
print(ult_ubicacion)


# EJERCICIO 3

lista_palabras = []

lista_palabras.append("Hola")
lista_palabras.append("Ok")
lista_palabras.append("Chau")

print(lista_palabras)


# EJERCICIO 4
animales = ["perro", "gato", "conejo", "pez"]

animales[1] = "loro"
animales[-1] = "oso"

print(animales)

# EJERCICIO 5
'''
    #El programa crea una lista de numeros y 
    #utiliza el remove para eliminar de la lista 
    #el numero mayor de la misma.
'''
numbers = [8, 15, 3, 22, 7]

numbers.remove(max(numbers))
print(numbers)


# EJERCICIO 6

lista6 = []

for i in range(10, 31, 5):
    lista6.append(i)

primeros_nros = lista6[0:2]
print(primeros_nros)



# EJERCICIO 7

autos = ["sedan", "polo", "suran", "gol"]

autos[1] = "fastback"
autos[2] = "hilux"
print(autos)

# EJERCICIO 8

dobles = []
dobles.append(5*2)
dobles.append(10*2)
dobles.append(15*2)
print(dobles)


# EJERCICIO 9

compras = [["pan", 'leche'], ["arroz", "fideos", "salsa"], ["agua"]]

compras[2].append("jugo")
compras[1][1] = "tallarines"
compras[0].remove("pan")
print(compras)
'''

# EJERCICIO 10

lista_anidada = [15, True, [25.5, 57.9, 30.6], False]
print(lista_anidada)