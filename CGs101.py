import matplotlib.pyplot as plt
import networkx as nx

# Create a directed graph
G = nx.DiGraph()

# Adding nodes to the graph
G.add_node("Dual Nature of Radiation and Matter")
G.add_node("Photoelectric Effect")


# Removed duplicate nodes for 'Photoelectric Effect'
G.add_node('Albert Einstein in 1905')
G.add_node('Emission of electrons from metal surface by light radiation')
# We can add as many as nodes.

# Adding edges with labels to the graph
G.add_edge("Dual Nature of Radiation and Matter", 'Photoelectric Effect', label='deals with')
G.add_edge('Photoelectric Effect', 'Wave Nature of Matter', label='cannot be explained by')
G.add_edge('Photoelectric Effect', 'Albert Einstein in 1905', label='discovered by')
G.add_edge('Photoelectric Effect', 'Emission of electrons from metal surface by light radiation', label='is')

# Positioning nodes using a spring layout
pos = nx.spring_layout(G)

# Drawing the graph with specified attributes
nx.draw(G, pos, with_labels=True, node_color='skyblue', node_size=1000, edge_color='black', linewidths=1, font_size=10)

# Drawing edge labels on the graph
edge_labels = nx.get_edge_attributes(G, 'label')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

# Displaying the graph
plt.show()
