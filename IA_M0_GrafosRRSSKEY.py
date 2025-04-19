import networkx as nx
import matplotlib.pyplot as plt
import numpy as np # Importar numpy para manejo de colores

# --- 1. Construyendo el Grafo con la Estructura Específica ---

# Creamos un grafo vacío
G = nx.Graph()

# --- Agregamos nodos con atributos de rol y empresa ---
# Empresa A: "Innovate Solutions" 💡
G.add_node("Ana García", role="Dueño 👑💼", empresa="Innovate Solutions 💡")
G.add_node("Roberto Pérez", role="Gerente 💪👔", empresa="Innovate Solutions 💡")
G.add_node("Laura Torres", role="Empleado Senior 🧑‍💻📄", empresa="Innovate Solutions 💡")
G.add_node("Miguel Sánchez", role="Empleado Junior 🧑‍💻📄", empresa="Innovate Solutions 💡")

# Empresa B: "Creative Minds" 🎨
G.add_node("Carlos López", role="Dueño 👑💼", empresa="Creative Minds 🎨")
G.add_node("Sofía Rodríguez", role="Gerente 💪👔", empresa="Creative Minds 🎨")
G.add_node("Diego Herrera", role="Empleado Senior 🧑‍💻📄", empresa="Creative Minds 🎨")
G.add_node("Elena Castro", role="Empleado Junior 🧑‍💻📄", empresa="Creative Minds 🎨")

# Empresa C: "Dynamic Ventures" 📈
G.add_node("Javier Rivas", role="Dueño 👑💼", empresa="Dynamic Ventures 📈")
G.add_node("Patricia Soto", role="Gerente 💪👔", empresa="Dynamic Ventures 📈")
G.add_node("Fernando Vargas", role="Empleado Senior 🧑‍💻📄", empresa="Dynamic Ventures 📈") # ¡Nuestro objetivo!
G.add_node("Isabel Flores", role="Empleado Junior 🧑‍💻📄", empresa="Dynamic Ventures 📈")

# --- Agregamos las conexiones (aristas) con PESOS según el planteamiento ---
# Los dueños NO se conocen directamente: SIN aristas entre Ana, Carlos, Javier

# Conexiones dentro de la Empresa A (pesos moderados/altos)
G.add_edge("Ana García", "Roberto Pérez", weight=4)
G.add_edge("Ana García", "Laura Torres", weight=3)
G.add_edge("Roberto Pérez", "Laura Torres", weight=5)
G.add_edge("Roberto Pérez", "Miguel Sánchez", weight=4)
G.add_edge("Laura Torres", "Miguel Sánchez", weight=3)

# Conexiones dentro de la Empresa B (pesos moderados/altos)
G.add_edge("Carlos López", "Sofía Rodríguez", weight=5)
G.add_edge("Carlos López", "Diego Herrera", weight=4)
G.add_edge("Sofía Rodríguez", "Diego Herrera", weight=4)
G.add_edge("Sofía Rodríguez", "Elena Castro", weight=3)
G.add_edge("Diego Herrera", "Elena Castro", weight=2)

# Conexiones dentro de la Empresa C (pesos moderados/altos)
G.add_edge("Javier Rivas", "Patricia Soto", weight=5)
G.add_edge("Javier Rivas", "Fernando Vargas", weight=4) # Conexión de Fernando con su dueño
G.add_edge("Patricia Soto", "Fernando Vargas", weight=4) # Conexión de Fernando con su gerente
G.add_edge("Patricia Soto", "Isabel Flores", weight=3)
G.add_edge("Fernando Vargas", "Isabel Flores", weight=3)

# --- ¡Conexiones ESTRATÉGICAS de Fernando Vargas! ---
G.add_edge("Fernando Vargas", "Ana García", weight=5) # Fernando conoce fuerte a Dueña A
G.add_edge("Fernando Vargas", "Carlos López", weight=5) # Fernando conoce fuerte a Dueño B
G.add_edge("Fernando Vargas", "Sofía Rodríguez", weight=4) # Fernando conoce fuerte a Gerente B

# --- Otras conexiones inter-empresas ---
G.add_edge("Roberto Pérez", "Sofía Rodríguez", weight=2) # Gerentes con conexión más débil
G.add_edge("Laura Torres", "Diego Herrera", weight=3) # Empleados Senior que se conocen
G.add_edge("Miguel Sánchez", "Elena Castro", weight=2) # Empleados Junior que se conocen
G.add_edge("Laura Torres", "Fernando Vargas", weight=3) # Conexión entre Empleados Senior
G.add_edge("Diego Herrera", "Fernando Vargas", weight=3) # Conexión entre Empleados Senior
G.add_edge("Elena Castro", "Fernando Vargas", weight=2) # Conexión entre Empleado Junior y Fernando

# --- 2. Visualizando la Red ---

# Definir colores para cada rol
color_map = {
    "Dueño 👑💼": "gold",
    "Gerente 💪👔": "salmon",
    "Empleado Senior 🧑‍💻📄": "lightblue",
    "Empleado Junior 🧑‍💻📄": "lightgreen"
}

# Obtener los colores de los nodos basados en su rol
node_colors = [color_map[G.nodes[node]['role']] for node in G.nodes()]

# Obtener los pesos de las aristas para visualizarlos
edge_weights = [G[u][v]['weight'] for u,v in G.edges()]

# Normalizar pesos para grosor de arista (opcional, para mejor visualización)
max_weight = max(edge_weights) if edge_weights else 1
normalized_weights = [w/max_weight * 4 for w in edge_weights] # Multiplicar por un factor para hacer las diferencias más visibles

plt.figure(figsize=(16, 14)) # Aumentar tamaño
pos = nx.spring_layout(G, k=0.7, iterations=50) # Ajustar k y iteraciones

# Dibujar nodos y aristas
nx.draw(G, pos, with_labels=True, node_color=node_colors, node_size=5000,
        edge_color='gray', width=normalized_weights, # Usar pesos normalizados para el grosor
        alpha=0.9, font_size=9, font_weight='bold')

# Agregar etiquetas de peso a las aristas
edge_labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=8, alpha=0.7, rotate=False)


# Crear una leyenda para los colores de los roles
handles = [plt.Line2D([0], [0], marker='o', color='w', label=role,
                      markerfacecolor=color_map[role], markersize=15)
           for role in color_map]
plt.legend(handles=handles, title="Roles", loc='upper left')

plt.title("Grafo de Red Social de Negocios (Estructura Diseñada) 📈👥", size=15)
plt.show()

# --- 3. Analizando Conexiones Fuertes y Clave ---

print("--- Calculando Centralidad ---")

# Calcular la Centralidad de Grado Ponderado
weighted_degree_centrality = dict(G.degree(weight='weight'))

# Calcular la Centralidad de Autovector (considerando los pesos)
try:
    # Aumentar max_iter y ajustar tol si es necesario para asegurar convergencia
    eigenvector_centrality = nx.eigenvector_centrality(G, weight='weight', max_iter=3000, tol=1e-7)
except nx.PowerIterationConvergenceError:
    print("\n¡Advertencia!: La Centralidad de Autovector no convergió después de muchas iteraciones.")
    print("Esto puede pasar en ciertos tipos de grafos. Considera aumentar max_iter o revisar la estructura.")
    eigenvector_centrality = None # O manejar el error de otra forma si es necesario
except Exception as e:
    print(f"\nOcurrió un error al calcular la Centralidad de Autovector: {e}")
    eigenvector_centrality = None

# Imprimir los resultados
print("\n--- Resultados de Centralidad ---")
print("Centralidad de Grado Ponderado:")
sorted_weighted_degree = sorted(weighted_degree_centrality.items(), key=lambda item: item[1], reverse=True)
for node, centrality in sorted_weighted_degree:
    print(f"  {node} ({G.nodes[node]['role']}, {G.nodes[node]['empresa']}): {centrality:.2f}")

if eigenvector_centrality:
    print("\nCentralidad de Autovector:")
    sorted_eigenvector = sorted(eigenvector_centrality.items(), key=lambda item: item[1], reverse=True)
    for node, centrality in sorted_eigenvector:
        print(f"  {node} ({G.nodes[node]['role']}, {G.nodes[node]['empresa']}): {centrality:.4f}")

# --- 4. Identificando al Puente Clave ---

print("\n--- Análisis para Identificar el Puente Clave ---")

if eigenvector_centrality:
    # El nodo con la centralidad de autovector más alta es nuestro puente clave en esta estructura
    # Aseguramos que hay nodos y que el cálculo fue exitoso
    if sorted_eigenvector:
        key_bridge_node, key_bridge_centrality = sorted_eigenvector[0]

        print(f"\nSegún el análisis de Centralidad de Autovector Ponderada:")
        print(f"  La persona más influyente y potencial puente clave es: 🎉 {key_bridge_node} 🎉")
        print(f"  Rol: {G.nodes[key_bridge_node]['role']}")
        print(f"  Empresa: {G.nodes[key_bridge_node]['empresa']}")
        print(f"  Centralidad de Autovector: {key_bridge_centrality:.4f}")

        print(f"\nSus conexiones estratégicas son clave:")
        # Mostrar conexiones con dueños y gerentes clave
        key_targets = ["Ana García", "Carlos López", "Javier Rivas", "Roberto Pérez", "Sofía Rodríguez", "Patricia Soto"]
        for neighbor, attributes in G[key_bridge_node].items():
             if neighbor in key_targets or G.nodes[neighbor]['role'] in ["Dueño 👑💼", "Gerente 💪👔"]:
                print(f"  - Conectado a: {neighbor} ({G.nodes[neighbor]['role']}, {G.nodes[neighbor]['empresa']}) con fuerza {attributes['weight']}")

        # Verificamos si es Fernando Vargas, como diseñamos
        if key_bridge_node == "Fernando Vargas":
             print("\n¡Exacto! 🎉 Como diseñamos el grafo, Fernando Vargas es identificado como el nodo más influyente.")
             print("Sus fuertes conexiones con los dueños de otras empresas y gerentes, a pesar de no ser un dueño él mismo, lo posicionan como un puente estratégico crucial.")
        else:
             print("\nInteresante. El análisis identificó a otra persona como la más influyente, lo que indica que la estructura de pesos y conexiones la favoreció aún más.")
             print("Revisa la Centralidad de Autovector para ver quién es y por qué sus conexiones son más influyentes en este grafo.")

    else:
        print("\nNo hay resultados de centralidad de autovector para analizar.")

else:
     print("\nNo se pudo realizar el análisis de Centralidad de Autovector para identificar al puente clave.")

print("\n¡Este análisis muestra cómo la estructura y la fuerza de las conexiones definen la influencia en una red! 📊💡")