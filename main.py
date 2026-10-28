from asyncio import graph

from circuit.circuit import Circuit
from circuit.components import Resistor, VoltageSource
# import networkx as nx

def main():
    circuit = Circuit()
    circuit.add_resistor("R1", "A", "B", 1000)
    circuit.add_resistor("R2", "B", "GND", 2000)
    circuit.add_resistor("R3", "B", "GND", 3000)
    circuit.add_voltage_source("V1", "A", "GND", 12)

    graph = circuit.to_graph()

    print(graph.number_of_nodes())
    print(graph.number_of_edges())
    for edge in list(graph.edges(keys=True, data=True)):
        print(edge)



if __name__ == "__main__":
    main()