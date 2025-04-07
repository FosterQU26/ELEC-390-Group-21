import networkx as nx
import math
import tkinter as tk
# Create the graph
G = nx.Graph()

# Node positions (scaled down for smaller screens)
SCALE = 0.6
nodes = {
    "Node 1": (472 * SCALE, 459 * SCALE),
    "Node 2": (327 * SCALE, 459 * SCALE),
    "Node 3": (237 * SCALE, 460 * SCALE),
    "Node 4": (154 * SCALE, 460 * SCALE),
    "Node 5": (603 * SCALE, 355 * SCALE),
    "Node 6": (472 * SCALE, 355 * SCALE),
    "Node 7": (327 * SCALE, 355 * SCALE),
    "Node 8": (237 * SCALE, 355 * SCALE),
    "Node 9": (154 * SCALE, 355 * SCALE),
    "Node 10": (54 * SCALE, 355 * SCALE),
    "Node 11": (603 * SCALE, 258 * SCALE),
    "Node 12": (472 * SCALE, 258 * SCALE),
    "Node 13": (327 * SCALE, 258 * SCALE),
    "Node 14": (237 * SCALE, 250 * SCALE),
    "Node 15": (181 * SCALE, 225 * SCALE),
    "Node 16": (604 * SCALE, 199 * SCALE),
    "Node 17": (472 * SCALE, 198 * SCALE),
    "Node 18": (327 * SCALE, 196 * SCALE),
    "Node 19": (296 * SCALE, 185 * SCALE),
    "Node 20": (372 * SCALE, 168 * SCALE),
    "Node 21": (54 * SCALE, 163 * SCALE),
    "Node 22": (612 * SCALE, 138 * SCALE),
    "Node 23": (595 * SCALE, 138 * SCALE),
    "Node 24": (357 * SCALE, 106 * SCALE),
    "Node 25": (306 * SCALE, 100 * SCALE),
    "Node 26": (472 * SCALE, 91 * SCALE),
    "Node 27": (205 * SCALE, 34 * SCALE),
    "Node 28": (472 * SCALE, 28 * SCALE),
    "Node 29": (472 * SCALE, 20 * SCALE),
}

# Add nodes to graph
for node, pos in nodes.items():
    G.add_node(node, pos=pos)

# Updated connections with requested changes
connections = [
    # Node 1 connections
    ("Node 1", "Node 2"), ("Node 1", "Node 6"), ("Node 1", "Node 5"),
    # Node 2 connections
    ("Node 2", "Node 3"), ("Node 2", "Node 1"), ("Node 2", "Node 7"),
    # Node 3 connections
    ("Node 3", "Node 8"), ("Node 3", "Node 4"), ("Node 3", "Node 2"),
    # Node 4 connections
    ("Node 4", "Node 10"), ("Node 4", "Node 9"), ("Node 4", "Node 3"),
    # Node 5 connections
    ("Node 5", "Node 1"), ("Node 5", "Node 6"), ("Node 5", "Node 11"),
    # Node 6 connections
    ("Node 6", "Node 1"), ("Node 6", "Node 5"), ("Node 6", "Node 7"), ("Node 6", "Node 12"),
    # Node 7 connections
    ("Node 7", "Node 2"), ("Node 7", "Node 6"), ("Node 7", "Node 8"), ("Node 7", "Node 13"),
    # Node 8 connections
    ("Node 8", "Node 3"), ("Node 8", "Node 9"), ("Node 8", "Node 14"), ("Node 8", "Node 7"),
    # Node 9 connections
    ("Node 9", "Node 4"), ("Node 9", "Node 10"), ("Node 9", "Node 15"), ("Node 9", "Node 8"),
    # Node 10 connections
    ("Node 10", "Node 4"), ("Node 10", "Node 9"), ("Node 10", "Node 21"),
    # Node 11 connections
    ("Node 11", "Node 5"), ("Node 11", "Node 12"), ("Node 11", "Node 16"),
    # Node 12 connections
    ("Node 12", "Node 6"), ("Node 12", "Node 13"), ("Node 12", "Node 17"), ("Node 12", "Node 11"),
    # Node 13 connections
    ("Node 13", "Node 14"), ("Node 13", "Node 12"), ("Node 13", "Node 18"), ("Node 13", "Node 7"),
    # Node 14 connections
    ("Node 14", "Node 15"), ("Node 14", "Node 8"), ("Node 14", "Node 19"), ("Node 14", "Node 13"),
    # Node 15 connections
    ("Node 15", "Node 21"), ("Node 15", "Node 9"), ("Node 15", "Node 14"), ("Node 15", "Node 27"),
    # Node 16 connections
    ("Node 16", "Node 11"), ("Node 16", "Node 17"), ("Node 16", "Node 22"), ("Node 16", "Node 23"),
    # Node 17 connections
    ("Node 17", "Node 12"), ("Node 17", "Node 20"), ("Node 17", "Node 26"), ("Node 17", "Node 16"),
    # Node 18 connections
    ("Node 18", "Node 19"), ("Node 18", "Node 20"), ("Node 18", "Node 13"),
    # Node 19 connections
    ("Node 19", "Node 14"), ("Node 19", "Node 18"), ("Node 19", "Node 25"),
    # Node 20 connections
    ("Node 20", "Node 18"), ("Node 20", "Node 24"), ("Node 20", "Node 17"),
    # Node 21 connections
    ("Node 21", "Node 10"), ("Node 21", "Node 15"), ("Node 21", "Node 27"),
    # Node 22 connections
    ("Node 22", "Node 29"), ("Node 22", "Node 16"), ("Node 22", "Node 23"),
    # Node 23 connections
    ("Node 23", "Node 26"), ("Node 23", "Node 23"), ("Node 23", "Node 16"),
    # Node 24 connections
    ("Node 24", "Node 25"), ("Node 24", "Node 29"), ("Node 24", "Node 20"),
    # Kept 24-29, removed 24-28 (wasn't present)
    # Node 25 connections
    ("Node 25", "Node 27"), ("Node 25", "Node 19"), ("Node 25", "Node 24"),
    # Node 26 connections
    ("Node 26", "Node 28"), ("Node 26", "Node 23"), ("Node 26", "Node 17"),
    # Node 27 connections
    ("Node 27", "Node 21"), ("Node 27", "Node 15"), ("Node 27", "Node 25"),
    # Node 28 connections
    ("Node 28", "Node 26"), ("Node 28", "Node 29"),  # Added 28-29 connection
    # Node 29 connections
    ("Node 29", "Node 24"), ("Node 29", "Node 28"), ("Node 29", "Node 22"),  # Kept 29-24, added 29-28
]

# Define special zones
risk_zone = [("Node 7", "Node 8"), ("Node 8", "Node 9")]
pedestrian_zone = [("Node 21", "Node 15"), ("Node 27", "Node 15"), ("Node 13", "Node 12")]

# Add edges with weights based on zones
for u, v in connections:
    x1, y1 = nodes[u]
    x2, y2 = nodes[v]
    distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

    # Apply zone-based weights
    if (u, v) in risk_zone or (v, u) in risk_zone:
        weight = distance * 5.0  # Highest weight for risk zone
    elif (u, v) in pedestrian_zone or (v, u) in pedestrian_zone:
        weight = distance * 2.0  # Medium weight for pedestrian zone
    else:
        weight = distance * 1.0  # Normal weight

    G.add_edge(u, v, weight=weight)


# A* heuristic function (Euclidean distance)
def heuristic(u, v):
    x1, y1 = nodes[u]
    x2, y2 = nodes[v]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)


# Create GUI
root = tk.Tk()
root.title("A* Pathfinding Visualization with Weighted Zones")
root.geometry("450x500")

canvas = tk.Canvas(root, width=400, height=400, bg='white')
canvas.pack(pady=10)

# Draw nodes
for i, (node, (x, y)) in enumerate(nodes.items()):
    canvas.create_oval(x - 6, y - 6, x + 6, y + 6, fill='lightblue', outline='black')
    canvas.create_text(x, y, text=str(i + 1), font=('Arial', 8))

# Draw edges with different styles based on zones
for u, v in connections:
    x1, y1 = nodes[u]
    x2, y2 = nodes[v]

    if (u, v) in risk_zone or (v, u) in risk_zone:
        # Red dashed line for risk zone
        canvas.create_line(x1, y1, x2, y2, fill='red', width=2, dash=(3, 2))
    elif (u, v) in pedestrian_zone or (v, u) in pedestrian_zone:
        # Green dotted line for pedestrian zone
        canvas.create_line(x1, y1, x2, y2, fill='green', width=1, dash=(2, 2))
    else:
        # Gray dotted line for normal connections
        canvas.create_line(x1, y1, x2, y2, fill='gray', width=1, dash=(2, 2))

# Add legend
legend = tk.Label(root, text="Red: Risk Zone (5x weight) | Green: Pedestrian Zone (2x weight)", font=('Arial', 8))
legend.pack()

# Pathfinding controls
control_frame = tk.Frame(root)
control_frame.pack()

tk.Label(control_frame, text="Start:").pack(side=tk.LEFT)
start_var = tk.StringVar(value="Node 1")
start_menu = tk.OptionMenu(control_frame, start_var, *nodes.keys())
start_menu.pack(side=tk.LEFT, padx=5)

tk.Label(control_frame, text="End:").pack(side=tk.LEFT, padx=(10, 0))
end_var = tk.StringVar(value="Node 29")
end_menu = tk.OptionMenu(control_frame, end_var, *nodes.keys())
end_menu.pack(side=tk.LEFT)


def find_path():
    start = start_var.get()
    end = end_var.get()

    # Temporarily remove direct edge if it exists
    direct_edge_removed = False
    if G.has_edge(start, end):
        G.remove_edge(start, end)
        direct_edge_removed = True

    try:
        # Find path using A*
        path = nx.astar_path(G, start, end, heuristic=heuristic, weight='weight')

        # Highlight the path
        canvas.delete("path")
        for i in range(len(path) - 1):
            x1, y1 = nodes[path[i]]
            x2, y2 = nodes[path[i + 1]]
            canvas.create_line(x1, y1, x2, y2, fill='blue', width=3, tags="path")

        # Highlight start and end nodes
        x, y = nodes[start]
        canvas.create_oval(x - 8, y - 8, x + 8, y + 8, outline='green', width=2, tags="path")
        x, y = nodes[end]
        canvas.create_oval(x - 8, y - 8, x + 8, y + 8, outline='red', width=2, tags="path")

    except nx.NetworkXNoPath:
        canvas.delete("path")
        canvas.create_text(200, 20, text="No path found!", fill='red', tags="path")

    # Restore direct edge if it was removed
    if direct_edge_removed:
        x1, y1 = nodes[start]
        x2, y2 = nodes[end]
        distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
        G.add_edge(start, end, weight=distance)


tk.Button(root, text="Find Path", command=find_path, bg='lightgreen').pack(pady=10)

root.mainloop()
