import networkx as nx

def main():
    graph = nx.MultiGraph()
    graph.add_node("A")
    graph.add_node("B")
    graph.add_node("GND")
    graph.add_edge("A", "B", key="R1", resistance=1000)
    graph.add_edge("B", "GND", key="R2", resistance=2000)
    graph.add_edge("B", "GND", key="R3", resistance=3000)
    # print("Nodes in the graph:", graph.nodes)
    # print("Number of nodes in the graph:", graph.number_of_nodes())
    # print("Edges in the graph:", list(graph.edges(keys=True, data=True)))
    # print("Number of edges in the graph:", graph.number_of_edges())

    # print(type(graph))
    # print(graph.is_multigraph())
    print(f"R2 resistance: {graph['B']['GND']['R2']['resistance']}")
    print(f"B neighbors: {list(graph.neighbors('B'))}")
    checknodes = []
    for node1, node2, key in graph.edges(keys=True):
        if key == "R2" or key == "R3":
            checknodes.append((node1, node2))
    if len(checknodes) == 2:
        same_nodes = set(checknodes[0]) == set(checknodes[1])
        print(f"R2 and R3 connect the same nodes: {same_nodes}")
    else:
        print("R2 or R3 was not found")
            

if __name__ == "__main__":
    main()
