import unittest
from circuit.components import Component, Resistor, VoltageSource


class TestResistor(unittest.TestCase):

    def test_valid_resistor(self):
        # Your implementation
        resistor = Resistor("R1", "A", "B", 1000)
        self.assertEqual(resistor.name, "R1")
        self.assertEqual(resistor.node1, "A")
        self.assertEqual(resistor.node2, "B")
        self.assertEqual(resistor.resistance, 1000)

    def test_invalid_resistor(self):
        invalid_cases = [
            ("R2", "A", "B", -100),
            ("R2", "A", "B", "1000"),
            (123, "A", "B", 1000),
            ("R4", "A", "A", 1000),
        ]

        for name, node1, node2, resistance in invalid_cases:
            with self.subTest(name=name, resistance=resistance):
                with self.assertRaises(ValueError):
                    Resistor(name, node1, node2, resistance)

    def test_invalid_node(self):
        with self.assertRaises(ValueError):
            Resistor("R1", "A", "A", 1000)

    def test_inheritance(self):
        resistor = Resistor("R1", "A", "B", 1000)
        self.assertIsInstance(resistor, Component)

if __name__ == "__main__":
    unittest.main()