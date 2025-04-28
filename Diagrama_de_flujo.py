import random
import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
import textwrap

# Personajes, armas, locaciones y las historias
personajes = ["Elena Duarte", "Marco Salazar", "Lucía Rivas", "Tomás Vélez", "Sofía Mendoza"]
armas = ["Cuchillo", "Pistola", "Veneno", "Estatua pesada", "Candelabro"]
locaciones = ["Cocina de la mansión", "Estudio privado", "Biblioteca", "Jardín", "Habitación principal"]

historias = {
    ("Elena Duarte", "Cuchillo", "Cocina de la mansión"): "Durante una acalorada discusión, Elena utilizó el cuchillo de cocina para cometer el crimen.",
    ("Marco Salazar", "Pistola", "Estudio privado"): "Marco, el detective, utilizó una pistola en el estudio privado para silenciar a la víctima.",
    ("Lucía Rivas", "Veneno", "Biblioteca"): "Lucía envenenó a su víctima mientras discutían sobre literatura en la biblioteca.",
    ("Tomás Vélez", "Estatua pesada", "Jardín"): "Tomás usó una estatua pesada en el jardín durante una discusión acalorada.",
    ("Sofía Mendoza", "Candelabro", "Habitación principal"): "Sofía dejó caer un candelabro antiguo sobre su rival en la habitación principal."
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

# Crear el grafo
G = nx.Graph()

# Agregar nodos para personaje, arma, locación e historia
G.add_node(culpable)
G.add_node(arma)
G.add_node(locacion)
G.add_node("Historia")  # Nodo de la historia

# Agregar conexiones entre los nodos
G.add_edge(culpable, arma)
G.add_edge(culpable, locacion)
G.add_edge(culpable, "Historia")

# Posiciones para el grafo (distribución en estrella)
pos = {
    culpable: (0, 0.5),
    arma: (-1, -0.5),
    locacion: (1, -0.5),
    "Historia": (0, -1.5)
}

# Preparar etiquetas de los nodos
historia_envuelta = "\n".join(textwrap.wrap(historias[(culpable, arma, locacion)], width=30))
labels = {
    culpable: culpable,
    arma: arma,
    locacion: locacion,
    "Historia": historia_envuelta
}

# Crear la figura
plt.figure(figsize=(7, 6))
nx.draw_networkx_nodes(G, pos, nodelist=[culpable], node_color="lightgreen", node_size=2500)
nx.draw_networkx_nodes(G, pos, nodelist=[arma, locacion, "Historia"], node_color="lightblue", node_size=2000)
nx.draw_networkx_edges(G, pos, width=2.0)
nx.draw_networkx_labels(G, pos, labels, font_size=10, font_weight="bold")

plt.title(f"Grafo de {culpable}", fontsize=16)
plt.axis('off')
plt.tight_layout()

# Guardar el grafo en un archivo PDF
with PdfPages('clue_game_graphs.pdf') as pdf:
    pdf.savefig()
    plt.close()

print("✅ El grafo ha sido generado y guardado en 'clue_game_graphs.pdf'.")
