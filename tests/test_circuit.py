import unittest
from circuit.circuit import Circuit


class TestCircuit(unittest.TestCase):

    def setUp(self):
        self.circuit = Circuit()

    def test_add_resistor(self):
        self.circuit.add_resistor("R1", "A", "B", 1000)
        self.assertIn("R1", self.circuit.components)
        self.assertEqual(self.circuit.components["R1"].resistance, 1000)

    def test_nodes(self):
        self.circuit.add_resistor("R1", "A", "B", 1000)
        self.circuit.add_resistor("R2", "B", "C", 2000)

        self.assertEqual(self.circuit.nodes, {"A", "B", "C"})

    def test_duplicate_name(self):
        self.circuit.add_resistor("R1", "A", "B", 1000)
        with self.assertRaises(ValueError):
            self.circuit.add_resistor("R1", "C", "D", 2000)
        self.assertEqual(self.circuit.components["R1"].resistance, 1000)
        self.assertEqual(self.circuit.nodes, {"A", "B"})

    def test_add_voltage_source(self):
        self.circuit.add_voltage_source("V1", "A", "GND", 12)
        self.assertIn("V1", self.circuit.components)
        self.assertEqual(self.circuit.components["V1"].voltage, 12)
        self.assertEqual(self.circuit.nodes, {"A", "GND"})

    def test_duplicate_across_types(self):
        self.circuit.add_resistor("R1", "A", "B", 1000)
        with self.assertRaises(ValueError):
            self.circuit.add_voltage_source("R1", "C", "D", 5)
        self.assertEqual(self.circuit.components["R1"].resistance, 1000)
        self.assertEqual(self.circuit.nodes, {"A", "B"})


if __name__ == "__main__":
    unittest.main()