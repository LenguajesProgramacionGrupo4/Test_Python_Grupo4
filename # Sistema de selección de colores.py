# Sistema de selección de colores

# Matriz de colores
colores = [
    ["Morado", "Azul", "Verde"],
    ["Negro", "Blanco", "Gris"],
    ["Rosado", "Amarillo", "Rojo"]
]

def mostrar_colores():
    print("\nMatriz de colores:")
    for fila in colores:
        print(fila)

def seleccionar_por_genero(genero):
    genero = genero.lower()
    
    if genero == "hombre":
        print("\nColores sugeridos para hombre:")
        print(colores[0] + colores[1])  # colores neutros y frios
    
    elif genero == "mujer":
        print("\nColores sugeridos para mujer:")
        print(colores[0] + colores[2])  # colores frios y calidos
    
    else:
        print("\nGénero no reconocido. Mostrando todos los colores:")
        for fila in colores:
            print(fila)

def seleccionar_color():
    try:
        fila = int(input("\nElige una fila (del 0 al 2): "))
        columna = int(input("Elige una columna (del 0 al 2): "))
        
        color = colores[fila][columna]
        print(f"\nSeleccionaste el color: {color}")
    
    except (IndexError, ValueError):
        print("Selección inválida")

# Orden
print("Sistema de selección de Colores")

genero = input("Ingresa tu género (hombre/mujer): ")
mostrar_colores()
seleccionar_por_genero(genero)
seleccionar_color()
