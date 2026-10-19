class ParityDetectorMealy:
    def __init__(self):
        # Initial state is 'E' (Even number of 1s seen so far)
        self.state = 'E'

    def process_bit(self, bit: str) -> str:
        if bit not in ('0', '1'):
            raise ValueError(f"Invalid bit: {bit}")

        if self.state == 'E':
            if bit == '1':
                self.state = 'O'
                return 'B'  # Odd count reached -> output B
            else:
                return 'A'  # Still even -> output A

        elif self.state == 'O':
            if bit == '1':
                self.state = 'E'
                return 'A'  # Back to even count -> output A
            else:
                return 'B'  # Still odd -> output B

    def run(self, input_string: str):
        output_symbols = []
        state_history = [self.state]

        for bit in input_string:
            out = self.process_bit(bit)
            output_symbols.append(out)
            state_history.append(self.state)

        return "".join(output_symbols), state_history


# --- Demonstration ---
if __name__ == "__main__":
    input_str = "10110"
    machine = ParityDetectorMealy()
    output_str, history = machine.run(input_str)

    print("=== ODD PARITY MEALY MACHINE ===")
    print(f"Input : {input_str}")
    print(f"Output: {output_str}")  # Result: BABBB
    print(f"States: {' -> '.join(history)}")