import networkx as nx
import matplotlib.pyplot as plt

def generar_grafo_viajeros_sendero():
    """Genera y muestra un grafo simple de viajeros en un sendero."""
    grafo = nx.Graph()
    nodos = ["Inicio del Sendero", "Refugio 1", "Mirador", "Cima de la Montaña", "Refugio 2", "Fin del Sendero"]
    grafo.add_nodes_from(nodos)
    aristas = [
        ("Inicio del Sendero", "Refugio 1", {"distancia": 5}),
        ("Refugio 1", "Mirador", {"distancia": 3}),
        ("Mirador", "Cima de la Montaña", {"distancia": 2}),
        ("Mirador", "Refugio 2", {"distancia": 4}),
        ("Refugio 2", "Fin del Sendero", {"distancia": 6}),
    ]
    grafo.add_edges_from(aristas)

    pos = nx.spring_layout(grafo, seed=42)  # Para una disposición consistente
    nx.draw(grafo, pos, with_labels=True, node_size=1500, node_color="lightgreen", font_size=10, font_weight="bold")
    nx.draw_networkx_edge_labels(grafo, pos, edge_labels=nx.get_edge_attributes(grafo, 'distancia'))
    plt.title("Grafo de Viajeros en un Sendero")
    plt.show()

def generar_grafo_viajeros_metro():
    """Genera y muestra un grafo simple de viajeros en un sistema de metro."""
    grafo = nx.Graph()
    nodos = ["Estación A", "Estación B", "Estación C", "Estación D", "Estación E"]
    grafo.add_nodes_from(nodos)
    aristas = [
        ("Estación A", "Estación B", {"linea": "Línea 1"}),
        ("Estación B", "Estación C", {"linea": "Línea 1"}),
        ("Estación B", "Estación D", {"linea": "Línea 2"}),
        ("Estación D", "Estación E", {"linea": "Línea 2"}),
    ]
    grafo.add_edges_from(aristas)

    pos = nx.circular_layout(grafo)
    nx.draw(grafo, pos, with_labels=True, node_size=1500, node_color="lightblue", font_size=10, font_weight="bold")
    nx.draw_networkx_edge_labels(grafo, pos, edge_labels=nx.get_edge_attributes(grafo, 'linea'))
    plt.title("Grafo de Viajeros en un Metro")
    plt.show()

def generar_grafo_viajeros_carreteras():
    """Genera y muestra un grafo simple de viajeros en un mapa de carreteras."""
    grafo = nx.Graph()
    nodos = ["Ciudad X", "Ciudad Y", "Ciudad Z", "Pueblo W"]
    grafo.add_nodes_from(nodos)
    aristas = [
        ("Ciudad X", "Ciudad Y", {"km": 150}),
        ("Ciudad Y", "Ciudad Z", {"km": 200}),
        ("Ciudad X", "Pueblo W", {"km": 80}),
        ("Pueblo W", "Ciudad Z", {"km": 120}),
    ]
    grafo.add_edges_from(aristas)

    pos = nx.spring_layout(grafo, seed=100)
    nx.draw(grafo, pos, with_labels=True, node_size=1500, node_color="lightcoral", font_size=10, font_weight="bold")
    nx.draw_networkx_edge_labels(grafo, pos, edge_labels=nx.get_edge_attributes(grafo, 'km'))
    plt.title("Grafo de Viajeros en Carreteras")
    plt.show()

if __name__ == "__main__":
    generar_grafo_viajeros_sendero()
    generar_grafo_viajeros_metro()
    generar_grafo_viajeros_carreteras()