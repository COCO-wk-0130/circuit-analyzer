import networkx as nx

def main():

    graph = nx.MultiGraph()

    graph.add_edge("A", "B", key="R1", resistance=1000)
    graph.add_edge("B", "GND", key="R2", resistance=2000)

    graph.add_edge("C", "D", key="R3", resistance=3000)
    graph.add_node("E")

    # grounded_nodes = set()
    # ungrounded_nodes = set()

    # for component in nx.connected_components(graph):
    #     # Your implementation
    #     print("Component:", component)
    #     if "GND" in component:
    #         grounded_nodes.update(component)
    #     else:
    #         ungrounded_nodes.update(component)

    # print("Grounded nodes:", grounded_nodes)
    # print("Ungrounded nodes:", ungrounded_nodes)   

    isolated_nodes = []

    for node in graph.nodes:
        # Your implementation
        if graph.degree(node) == 0:
            isolated_nodes.append(node)

    print("Isolated nodes:", isolated_nodes)

    print("Isolated nodes (using nx.isolates):", list(nx.isolates(graph)))
    

if __name__ == "__main__":
    main()
