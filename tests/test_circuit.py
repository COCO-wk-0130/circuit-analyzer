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

    def test_to_graph(self):
        self.circuit.add_resistor("R1", "A", "B", 1000)
        self.circuit.add_resistor("R2", "B", "GND", 2000)
        self.circuit.add_resistor("R3", "B", "GND", 3000)
        self.circuit.add_voltage_source("V1", "A", "GND", 12)

        graph = self.circuit.to_graph()

        self.assertEqual(graph.number_of_nodes(), 3)
        self.assertEqual(graph.number_of_edges(), 4)

        self.assertTrue(graph.has_edge("B", "GND", key="R2"))
        self.assertTrue(graph.has_edge("B", "GND", key="R3"))

        checknodes = []
        for node1, node2, key, data in graph.edges(keys=True, data=True):
            if key == "R2" or key == "R3":
                checknodes.append((node1, node2))

        self.assertEqual(len(checknodes), 2)
        self.assertEqual(set(checknodes[0]), set(checknodes[1]))

        self.assertEqual(graph["A"]["B"]["R1"]["resistance"], 1000)
        self.assertEqual(graph["A"]["GND"]["V1"]["voltage"], 12)

        self.assertEqual(
            graph["A"]["B"]["R1"]["type"],
            "resistor"
        )

        self.assertEqual(
            graph["A"]["GND"]["V1"]["type"],
            "voltage_source"
        )


if __name__ == "__main__":
    unittest.main()