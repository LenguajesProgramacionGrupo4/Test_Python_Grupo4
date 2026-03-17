"""
Razas de perros y su país de origen
"""

# Diccionario de razas organizadas por país de origen
razas_por_pais = {
    "Alemania": [
        "Pastor Alemán", "Rottweiler", "Dóberman", "Gran Danés",
        "Dachshund (Salchicha)", "Pinscher Alemán", "Spitz Alemán",
        "Weimaraner", "Boxer", "Schnauzer"
    ],
    "Reino Unido": [
        "Bulldog Inglés", "Beagle", "Golden Retriever", "Border Collie",
        "Labrador Retriever", "Yorkshire Terrier", "Springer Spaniel",
        "Setter Irlandés", "Bull Terrier", "Cocker Spaniel"
    ],
    "Francia": [
        "Bulldog Francés", "Bichón Frisé", "Briard", "Basset Hound",
        "Gran Gascón Saintongeois", "Papillón", "Boyero de Flandes"
    ],
    "Japón": [
        "Shiba Inu", "Akita Inu", "Hokkaido", "Kishu",
        "Tosa Inu", "Kai Ken", "Spitz Japonés"
    ],
    "China": [
        "Chow Chow", "Pekingese (Pequinés)", "Shar Pei",
        "Shih Tzu", "Pug (Carlino)"
    ],
    "Australia": [
        "Australian Cattle Dog (Heeler)", "Pastor Australiano",
        "Kelpie Australiano", "Silky Terrier Australiano"
    ],
    "Rusia": [
        "Borzoi (Lebrel Ruso)", "Samoyedo", "Husky Siberiano",
        "Laika Rusa", "Ovcharka del Cáucaso"
    ],
    "Estados Unidos": [
        "American Pit Bull Terrier", "Boykin Spaniel",
        "Catahoula Leopard Dog", "Plott Hound", "Boston Terrier"
    ],
    "Suiza": [
        "Bernés de la Montaña", "San Bernardo",
        "Gran Boyero Suizo", "Appenzeller"
    ],
    "Irlanda": [
        "Irish Wolfhound", "Kerry Blue Terrier",
        "Glen of Imaal Terrier", "Irish Water Spaniel"
    ],
    "España": [
        "Galgo Español", "Mastín Español",
        "Podenco Ibicenco", "Perro de Agua Español"
    ],
    "México": [
        "Xoloitzcuintli (Perro sin pelo mexicano)",
        "Chihuahua"
    ],
    "Canadá": [
        "Labrador Retriever", "Terranova (Newfoundland)",
        "Perro de trineo del Canadá"
    ],
    "Grecia": [
        "Perro de Caza Griego (Hellenikos Ichnilatis)"
    ],
    "Corea": [
        "Jindo Coreano"
    ],
    "India": [
        "Rajapalayam", "Mudhol Hound", "Kanni"
    ],
    "África del Sur": [
        "Rhodesian Ridgeback", "Basenji"
    ],
}

# Lista plana de todas las razas con su país
todas_las_razas = []
for pais, razas in razas_por_pais.items():
    for raza in razas:
        todas_las_razas.append({"raza": raza, "pais": pais})

# ─────────────────────────────────────────────
# MENÚ DE OPCIONES
# ─────────────────────────────────────────────

def mostrar_todas():
    """Muestra todas las razas con su país de origen."""
    print(f"\n{'─'*50}")
    print(f"{'RAZA':<35} {'PAÍS'}")
    print(f"{'─'*50}")
    for item in sorted(todas_las_razas, key=lambda x: x["raza"]):
        print(f"{item['raza']:<35} {item['pais']}")
    print(f"{'─'*50}")
    print(f"Total: {len(todas_las_razas)} razas registradas.\n")


def mostrar_por_pais():
    """Muestra las razas agrupadas por país."""
    print(f"\n{'═'*50}")
    for pais, razas in sorted(razas_por_pais.items()):
        print(f"\n  {pais.upper()}")
        print(f"{'─'*40}")
        for raza in razas:
            print(f"   • {raza}")
    print(f"\n{'═'*50}\n")


def buscar_raza():
    """Busca un país dado el nombre de la raza."""
    nombre = input("Ingresa el nombre de la raza: ").strip().lower()
    encontrados = [
        item for item in todas_las_razas
        if nombre in item["raza"].lower()
    ]
    if encontrados:
        print(f"\n  Resultados para '{nombre}':")
        for item in encontrados:
            print(f"  {item['raza']}  →  País de origen: {item['pais']}")
    else:
        print(f"\n  No se encontró ninguna raza con '{nombre}'.")
    print()


def buscar_por_pais():
    """Busca todas las razas de un país específico."""
    nombre_pais = input("Ingresa el nombre del país: ").strip().lower()
    encontrados = {
        pais: razas
        for pais, razas in razas_por_pais.items()
        if nombre_pais in pais.lower()
    }
    if encontrados:
        for pais, razas in encontrados.items():
            print(f"\n   Razas originarias de {pais}:")
            for raza in razas:
                print(f"     • {raza}")
    else:
        print(f"\n  No se encontraron razas del país '{nombre_pais}'.")
    print()


# ─────────────────────────────────────────────
# PROGRAMA PRINCIPAL
# ─────────────────────────────────────────────

def main():
    while True:
        print("╔══════════════════════════════════════╗")
        print("║     RAZAS DE PERROS POR PAÍS     ║")
        print("╠══════════════════════════════════════╣")
        print("║  1. Ver todas las razas (tabla)      ║")
        print("║  2. Ver razas agrupadas por país     ║")
        print("║  3. Buscar raza por nombre           ║")
        print("║  4. Buscar razas por país            ║")
        print("║  5. Salir                            ║")
        print("╚══════════════════════════════════════╝")

        opcion = input("Elige una opción (1-5): ").strip()

        if opcion == "1":
            mostrar_todas()
        elif opcion == "2":
            mostrar_por_pais()
        elif opcion == "3":
            buscar_raza()
        elif opcion == "4":
            buscar_por_pais()
        elif opcion == "5":
            print("\n¡Hasta luego! \n")
            break
        else:
            print("\n  Opción no válida. Intenta de nuevo.\n")


if __name__ == "__main__":
    main()