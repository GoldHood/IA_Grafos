import networkx as nx
import matplotlib.pyplot as plt

# Crear un grafo dirigido vacío
grafo_dirigido = nx.DiGraph()

# Agregar nodos
grafo_dirigido.add_nodes_from(["A", "B", "C", "D"])

# Agregar aristas dirigidas con pesos
grafo_dirigido.add_edge("A", "B", weight=2)
grafo_dirigido.add_edge("B", "C", weight=3)
grafo_dirigido.add_edge("C", "A", weight=10)
grafo_dirigido.add_edge("D", "C", weight=4)

# Imprimir información del grafo dirigido
print(f"Número de nodos: {grafo_dirigido.number_of_nodes()}")
print(f"Número de aristas: {grafo_dirigido.number_of_edges()}")
print(f"Nodos: {list(grafo_dirigido.nodes())}")
print(f"Aristas: {list(grafo_dirigido.edges())}")
print(f"Grado de salida de 'A': {grafo_dirigido.out_degree('A')}")
print(f"Grado de entrada de 'C': {grafo_dirigido.in_degree('C')}")
print(f"Sucesores de 'B': {list(grafo_dirigido.successors('B'))}")
print(f"Predecesores de 'A': {list(grafo_dirigido.predecessors('A'))}")
print(f"Atributos de la arista ('A', 'B'): {grafo_dirigido.get_edge_data('A', 'B')}")

# Visualizar el grafo dirigido
pos = nx.spring_layout(grafo_dirigido, seed=42)
nx.draw(grafo_dirigido, pos, with_labels=True, node_size=1500, node_color="lightcyan", font_size=10, font_weight="bold", arrowstyle='->', arrowsize=20)
nx.draw_networkx_edge_labels(grafo_dirigido, pos, edge_labels=nx.get_edge_attributes(grafo_dirigido, 'weight'))
plt.title("Ejemplo de Grafo Dirigido")
plt.show()