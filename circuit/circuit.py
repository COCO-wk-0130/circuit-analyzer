from circuit.components import Resistor, VoltageSource


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
        