import networkx as nx
import matplotlib.pyplot as plt

# --- 4. Construyendo el Grafo en Python ---

# Creamos un grafo vacío
G = nx.Graph()

# Agregamos nodos con atributos de rol
G.add_node("Empresario_A", role="Empresario 👑💼")
G.add_node("Empresario_B", role="Empresario 👑💼")
G.add_node("Jefe_1", role="Jefe 💪👔")
G.add_node("Jefe_2", role="Jefe 💪👔")
G.add_node("Jefe_3", role="Jefe 💪👔")
G.add_node("Empleado_X", role="Empleado 🧑‍💻📄")
G.add_node("Empleado_Y", role="Empleado 🧑‍💻📄")
G.add_node("Empleado_Z", role="Empleado 🧑‍💻📄")
G.add_node("Empleado_W", role="Empleado 🧑‍💻📄")
G.add_node("Empleado_V", role="Empleado 🧑‍💻📄")

# Agregamos las conexiones (aristas) - ¡Modifica estas según tu dibujo!
G.add_edge("Empresario_A", "Jefe_1")
G.add_edge("Empresario_A", "Jefe_2")
G.add_edge("Empresario_B", "Jefe_3")
G.add_edge("Jefe_1", "Empleado_X")
G.add_edge("Jefe_1", "Empleado_Y")
G.add_edge("Jefe_2", "Empleado_Z")
G.add_edge("Jefe_2", "Empleado_W")
G.add_edge("Jefe_3", "Empleado_V")
G.add_edge("Empleado_X", "Empleado_Y")
G.add_edge("Empleado_Z", "Empleado_W")
G.add_edge("Jefe_1", "Jefe_2") # Conexión entre jefes
G.add_edge("Empresario_A", "Empresario_B") # Conexión entre empresarios
G.add_edge("Jefe_1", "Jefe_3") # Ejemplo adicional de conexión

# --- 5. Visualizando la Red ---

# Definir colores para cada rol
color_map = {
    "Empresario 👑💼": "gold",
    "Jefe 💪👔": "salmon",
    "Empleado 🧑‍💻📄": "lightblue"
}

# Obtener los colores de los nodos basados en su rol
node_colors = [color_map[G.nodes[node]['role']] for node in G.nodes()]

# Dibujar el grafo
plt.figure(figsize=(12, 10)) # Aumentar tamaño de la figura
pos = nx.spring_layout(G, k=0.5) # Ajustar el parámetro k para el espaciado
nx.draw(G, pos, with_labels=True, node_color=node_colors, node_size=4000, edge_color='gray', alpha=0.9, font_size=10, width=1.5) # Aumentar node_size y width

# Crear una leyenda para los colores
handles = [plt.Line2D([0], [0], marker='o', color='w', label=role,
                      markerfacecolor=color_map[role], markersize=15)
           for role in color_map]
plt.legend(handles=handles, title="Roles", loc='upper right')

plt.title("Grafo de Nuestra Red Social 📈👥")
plt.show()

# --- 6. Encontrando Conexiones Importantes ---

# Calcular la centralidad de grado
degree_centrality = nx.degree_centrality(G)

# Imprimir la centralidad de grado de cada nodo
print("Centralidad de Grado:")
for node, centrality in degree_centrality.items():
    print(f"  {node} ({G.nodes[node]['role']}): {centrality:.2f}")

# --- 7. Identificando Key Business Access Points ---

# Encontrar los nodos con la centralidad de grado más alta
max_centrality = max(degree_centrality.values())
most_connected_nodes = [node for node, centrality in degree_centrality.items() if abs(centrality - max_centrality) < 1e-9] # Usar tolerancia para comparación de flotantes

print(f"\nLa persona/s más conectada/s (con la centralidad de grado más alta) es/son: {most_connected_nodes} 🎉")

# Opcional: Ordenar por centralidad de grado descendente
sorted_centrality = sorted(degree_centrality.items(), key=lambda item: item[1], reverse=True)
print("\nCentralidad de Grado (Ordenada):")
for node, centrality in sorted_centrality:
     print(f"  {node} ({G.nodes[node]['role']}): {centrality:.2f}")