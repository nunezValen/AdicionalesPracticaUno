import random

# Función para generar una galaxia ficticia
def generar_galaxia(num_estrellas):
    galaxia = []
    for _ in range(num_estrellas):
        # Generar coordenadas aleatorias para las estrellas
        x = random.randint(-50, 50)
        y = random.randint(-50, 50)
        galaxia.append((x, y))
    return galaxia

# Función para mostrar la galaxia en la consola
def mostrar_galaxia(galaxia):
    for y in range(-50, 51):
        for x in range(-50, 51):
            if (x, y) in galaxia:
                print("*", end="")
            else:
                print(" ", end="")
        print()

# Generar una galaxia con 100 estrellas
galaxia = generar_galaxia(100)

# Mostrar la galaxia en la consola
mostrar_galaxia(galaxia)