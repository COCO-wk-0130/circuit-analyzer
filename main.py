from asyncio import graph

from circuit.circuit import Circuit
from circuit.components import Resistor, VoltageSource
# import networkx as nx

def main():
    circuit = Circuit()

    circuit.add_resistor("R1", "A", "GND", 1000)
    circuit.add_resistor("R2", "C", "D", 2000)

    print(circuit.get_ungrounded_nodes())
    # {'C', 'D'}



if __name__ == "__main__":
    main()