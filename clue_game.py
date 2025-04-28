import random

# Personajes, armas y locaciones
personajes = ["Elena Duarte", "Marco Salazar", "Lucía Rivas", "Tomás Vélez", "Sofía Mendoza"]
armas = ["Cuchillo", "Pistola", "Veneno", "Estatua pesada", "Candelabro"]
locaciones = ["Cocina de la mansión", "Estudio privado", "Biblioteca", "Jardín", "Habitación principal"]

# Historias
historias = {
    ("Elena Duarte", "Cuchillo", "Cocina de la mansión"):
        "Durante una acalorada discusión, Elena utilizó el cuchillo de cocina para cometer el crimen.",
    ("Marco Salazar", "Pistola", "Estudio privado"):
        "Marco, el detective, utilizó una pistola en el estudio privado para silenciar a la víctima.",
    ("Lucía Rivas", "Veneno", "Biblioteca"):
        "Lucía envenenó a su víctima mientras discutían sobre literatura en la biblioteca.",
    ("Tomás Vélez", "Estatua pesada", "Jardín"):
        "Tomás usó una estatua pesada en el jardín durante una discusión acalorada.",
    ("Sofía Mendoza", "Candelabro", "Habitación principal"):
        "Sofía dejó caer un candelabro antiguo sobre su rival en la habitación principal."
}

# Pistas sutiles para cada combinación
pistas = {
    ("Elena Duarte", "Cuchillo", "Cocina de la mansión"): "Pista: El crimen ocurrió cerca de donde se preparaban comidas deliciosas.",
    ("Marco Salazar", "Pistola", "Estudio privado"): "Pista: El detective sabía más de lo que parecía.",
    ("Lucía Rivas", "Veneno", "Biblioteca"): "Pista: El veneno se sirvió en una bebida elegante mientras discutían libros.",
    ("Tomás Vélez", "Estatua pesada", "Jardín"): "Pista: El crimen ocurrió en un lugar rodeado de belleza natural.",
    ("Sofía Mendoza", "Candelabro", "Habitación principal"): "Pista: La habitación estaba decorada con antigüedades valiosas."
}

# Selección aleatoria
culpable = random.choice(personajes)
arma = random.choice(armas)
locacion = random.choice(locaciones)

# Asegurarse que sea una historia válida
while (culpable, arma, locacion) not in historias:
    culpable = random.choice(personajes)
    arma = random.choice(armas)
    locacion = random.choice(locaciones)

# Juego
print("\n¡Bienvenido al juego de Clue!")
print("Debes adivinar el CULPABLE, el ARMA y la LOCACIÓN del crimen.")
print("Tienes 3 intentos para resolverlo.")

intentos = 3

while intentos > 0:
    print(f"\nIntentos restantes: {intentos}")
    sospechoso = input(f"¿Quién fue el culpable? {personajes}: ")
    arma_usada = input(f"¿Con qué arma? {armas}: ")
    lugar = input(f"¿Dónde ocurrió? {locaciones}: ")

    # Pistas si el jugador está cerca de la respuesta
    if sospechoso != culpable and arma_usada == arma and lugar == locacion:
        print("\n🔍 Pista: Estás cerca, acertaste el arma y la locación.")
        print(f"Tu pista adicional: {pistas[(culpable, arma, locacion)]}")

    elif sospechoso == culpable and arma_usada != arma and lugar == locacion:
        print("\n🔍 Pista: Estás cerca, acertaste al culpable y la locación.")
        print(f"Tu pista adicional: {pistas[(culpable, arma, locacion)]}")

    elif sospechoso == culpable and arma_usada == arma and lugar != locacion:
        print("\n🔍 Pista: Estás cerca, acertaste al culpable y el arma.")
        print(f"Tu pista adicional: {pistas[(culpable, arma, locacion)]}")

    # Comprobación de la respuesta
    if (sospechoso, arma_usada, lugar) == (culpable, arma, locacion):
        print("\n🎉 ¡Correcto! Has resuelto el misterio.")
        print(f"\nHistoria final:\n{historias[(culpable, arma, locacion)]}")
        break
    else:
        print("\n❌ Esa no es la combinación correcta. Intenta de nuevo.")
        intentos -= 1

if intentos == 0:
    print("\n💀 Se acabaron los intentos. ¡El misterio sigue sin resolverse!")
    print(f"\nLa solución era:\nCulpable: {culpable}, Arma: {arma}, Locación: {locacion}")
    print(f"Historia final:\n{historias[(culpable, arma, locacion)]}")
