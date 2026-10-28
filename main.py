from circuit.circuit import Circuit

def main():
    circuit = Circuit()
    circuit.add_resistor("R1", "A", "B", 1000)
    circuit.add_voltage_source("V1", "A", "GND", 12)

    print(circuit.components.keys())
    # dict_keys(['R1', 'V1'])

    print(circuit.nodes)
    # {'A', 'B', 'GND'}  (order may vary)


if __name__ == "__main__":
    main()