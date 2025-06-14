# EJERCICIO 1
precio_frutas = {'Banana': 1200, 'Anana': 2500, 'Melon': 3000, 'Uva': 1450}

precio_frutas['Naranja'] = 1200
precio_frutas['Manzana'] = 1500
precio_frutas['Pera'] = 2300

print(precio_frutas)

# EJERCICIO 2
precio_frutas['Banana'] = 1330
precio_frutas['Manzana'] = 1700
precio_frutas['Melon'] = 2800

print(precio_frutas)

# EJERCICIO 3
lista_frutas = list(precio_frutas.keys())
print(f'Lista frutas: \n{lista_frutas}')

# EJERCICIO 4
# Create an empty dictionary to store contacts
agenda_telefonica = {}

print("--- Carga de Contactos ---")
# Allow the user to enter 5 contacts
for i in range(5):
    while True:
        nombre = input(f"Ingresa el nombre del contacto {i+1}: ").strip()
        if nombre: # Ensure the name is not empty
            break
        else:
            print("El nombre no puede estar vacío. Intenta de nuevo.")

    while True:
        numero = input(f"Ingresa el número de teléfono de {nombre}: ").strip()
        if numero.isdigit(): # Ensure the number contains only digits
            break
        else:
            print("El número de teléfono debe contener solo dígitos. Intenta de nuevo.")

    agenda_telefonica[nombre] = numero
    print(f"Contacto '{nombre}' agregado.\n")

print("--- Consulta de Contactos ---")
# Ask for a name and display the associated number
while True:
    nombre_buscar = input("Ingresa el nombre del contacto que deseas buscar (o 'salir' para terminar): ").strip()

    if nombre_buscar.lower() == 'salir':
        print("Saliendo del programa.")
        break
    elif not nombre_buscar:
        print("El nombre no puede estar vacío. Intenta de nuevo.")
        continue

    # Check if the name exists in the dictionary
    if nombre_buscar in agenda_telefonica:
        print(f"El número de teléfono de '{nombre_buscar}' es: {agenda_telefonica[nombre_buscar]}")
    else:
        print(f"Lo siento, el contacto '{nombre_buscar}' no se encontró en tu agenda.")
    print("-" * 30) # Separator for better readability