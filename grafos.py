import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
import textwrap

# Datos (personaje, arma, escenario, historia)
personajes = ["Elena Duarte", "Marco Salazar", "Lucía Rivas", "Tomás Vélez", "Sofía Mendoza"]
armas = ["Cuchillo", "Pistola", "Veneno", "Estatua pesada", "Candelabro"]
locaciones = ["Cocina de la mansión", "Estudio privado", "Biblioteca", "Jardín", "Habitación principal"]

historias = {
    ("Elena Duarte", "Cuchillo", "Cocina de la mansión"): "Durante una discusión, Elena utilizó un cuchillo en la cocina.",
    ("Marco Salazar", "Pistola", "Estudio privado"): "Marco, el detective, usó una pistola en el estudio.",
    ("Lucía Rivas", "Veneno", "Biblioteca"): "Lucía envenenó a su víctima en la biblioteca.",
    ("Tomás Vélez", "Estatua pesada", "Jardín"): "Tomás golpeó a su rival con una estatua en el jardín.",
    ("Sofía Mendoza", "Candelabro", "Habitación principal"): "Sofía dejó caer un candelabro en la habitación principal."
}

# Función para generar un grafo de la historia de un personaje
def generar_grafo(culpable, arma, locacion, historia):
    G = nx.Graph()
    G.add_node(culpable)
    G.add_node(arma)
    G.add_node(locacion)
    G.add_node("Historia")  # Nodo genérico para la historia

    # Crear conexiones
    G.add_edge(culpable, arma)
    G.add_edge(culpable, locacion)
    G.add_edge(culpable, "Historia")

    # Posiciones personalizadas (forma de estrella)
    pos = {
        culpable: (0, 0.5),
        arma: (-1, -0.5),
        locacion: (1, -0.5),
        "Historia": (0, -1.5)
    }

    # Etiquetas (historia más corta para que quepa)
    historia_envuelta = "\n".join(textwrap.wrap(historia, width=30))
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

    return plt

# Crear el PDF para guardar todos los grafos
with PdfPages('grafos_completos_personajes.pdf') as pdf:
    # Generar el grafo para cada combinación de personaje, arma y locación
    for personaje, arma, locacion in historias.keys():
        historia = historias[(personaje, arma, locacion)]
        
        # Generar el grafo de este personaje
        plt = generar_grafo(personaje, arma, locacion, historia)

        # Guardar la figura en el PDF
        pdf.savefig()
        plt.close()

print("✅ Todos los grafos fueron creados y guardados en 'grafos_completos_personajes.pdf'")
