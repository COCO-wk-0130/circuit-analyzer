from circuit.components import Resistor, VoltageSource
import networkx as nx


class Circuit:
    def __init__(self):
        self.components = {}
        self.nodes = set()

    def add_component(self, component):
        if component.name in self.components:
            raise ValueError(
                f"Component '{component.name}' already exists"
            )

        self.components[component.name] = component
        self.nodes.update([component.node1, component.node2])

    def add_resistor(self, name, node1, node2, resistance):
        resistor = Resistor(name, node1, node2, resistance)
        self.add_component(resistor)

    def add_voltage_source(self, name, node1, node2, voltage):
        source = VoltageSource(name, node1, node2, voltage)
        self.add_component(source)

    def to_graph(self):
        graph = nx.MultiGraph()

        for node in self.nodes:
            graph.add_node(node)

        for name in self.components:
            component = self.components[name]
            if isinstance(component, Resistor):
                graph.add_edge(
                    component.node1,
                    component.node2,
                    key=component.name,
                    type="resistor",
                    resistance=component.resistance
                )
            elif isinstance(component, VoltageSource):
                graph.add_edge(
                    component.node1,
                    component.node2,
                    key=component.name,
                    type="voltage_source",
                    voltage = component.voltage
                )
        return graph
        