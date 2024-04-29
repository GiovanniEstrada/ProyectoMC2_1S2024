import networkx as nx 
import tkinter as tk
from  tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

def draw_graph(bfs_edges=None):
    ax.clear()
    if bfs_edges:
        pos = nx.spring_layout(G)
        nx.draw(G, pos=pos, ax=ax, with_labels=True)
        nx.draw_networkx_edges(G, pos=pos, edgelist=bfs_edges, edge_color='g', ax=ax)
        nx.draw_networkx_nodes(G, pos=pos, nodelist=[startpos.get()]+[v for u, v in bfs_edges], node_color='g', ax=ax)
    else:
        nx.draw(G, ax=ax, with_labels=True)
        canvas.draw()

def show_bfs():
    sorted(G.nodes())
    bfs_edges=list(nx.bfs_edges(G,source=startpos.get()))
    draw_graph(bfs_edges)
    canvas.draw()

def show_dfs():
    sorted(G.nodes())
    bfs_edges=list(nx.dfs_edges(G,source=startpos.get()))
    draw_graph(bfs_edges)
    canvas.draw()
    

G = nx.Graph()
root = tk.Tk()
style = ttk.Style()
style.configure("TButton", font=("Helvetica", 12), width=15, height=2)

# Crear los botones
root.title("Algoritmo de busqueda en Anchura")

vertex_entry = tk.Entry(root, width=30)
vertex_entry.grid(row=1, column=0, columnspan=3, pady=10, padx=10)
add_vertex_button = ttk.Button(root, text="Agregar vértice", command=lambda: G.add_node(vertex_entry.get()))
add_vertex_button.grid(row=2, column=0, columnspan=3, pady=10, padx=10)

edge_entry_1 = tk.Entry(root, width=30)
edge_entry_2 = tk.Entry(root, width=30)
edge_entry_1.grid(row=3, column=0, padx=10, pady=10)
tk.Label(root, text="->").grid(row=3, column=1)  # Flecha en el medio
edge_entry_2.grid(row=3, column=2, padx=10, pady=10)
add_edge_button = ttk.Button(root, text="Agregar arista", command=lambda: G.add_edge(edge_entry_1.get(), edge_entry_2.get()))
add_edge_button.grid(row=4, column=0, columnspan=3, pady=10)

figure = Figure(figsize=(5,5))
ax = figure.add_subplot(111)
canvas=FigureCanvasTkAgg(figure, root)
canvas.get_tk_widget().grid(row=6, column=0, columnspan=3)

lblstartpos = tk.Label(root, text="Posición inicial")
lblstartpos.grid(row=7, column=0)
startpos = tk.Entry(root, width=30)
startpos.grid(row=7, column=1, columnspan=3, pady=10, padx=10)

draw_button = ttk.Button(root, text="Dibujar grafo", command=draw_graph)
draw_button.grid(row=8, column=0, pady=10)

bfs_button = ttk.Button(root, text="Busq. anchura", command=show_bfs)
bfs_button.grid(row=8, column=1, pady=10)

dfs_button = ttk.Button(root, text="Busq. profundidad", command=show_dfs)
dfs_button.grid(row=8, column=2, pady=10)
root.mainloop()