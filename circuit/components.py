import math

class Component:
    def __init__(self, name, node1, node2):
        if not isinstance(name, str) or not name.strip():
            raise ValueError("Name must be a non-empty string")

        if not isinstance(node1, str) or not isinstance(node2, str):
            raise ValueError("Node identifiers must be strings")

        if node1 == node2:
            raise ValueError("A component cannot connect to itself")

        self.name = name
        self.node1 = node1
        self.node2 = node2

class Resistor(Component):
    def __init__(self, name, node1, node2, resistance):
        super().__init__(name, node1, node2)
        if (
            isinstance(resistance, bool)
            or not isinstance(resistance, (int, float))
            or not math.isfinite(resistance)
        ):
            raise ValueError("Resistance must be a finite number")
        if resistance <= 0:
            raise ValueError("Resistance must be a positive number")

        self.resistance = resistance


class VoltageSource(Component):
    def __init__(self, name, node1, node2, voltage):
        super().__init__(name, node1, node2)
        if (
            isinstance(voltage, bool)
            or not isinstance(voltage, (int, float))
            or not math.isfinite(voltage)
        ):
            raise ValueError("Voltage must be a finite number")

        self.voltage = voltage