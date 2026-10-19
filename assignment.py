class ParityDetectorMealy:
    def __init__(self):
        # Initial state is 'E' (Even number of 1s seen so far, count = 0)
        self.state = 'E'

    def process_bit(self, bit: str) -> str:
        if bit not in ('0', '1'):
            raise ValueError(f"Invalid bit: {bit}")

        if self.state == 'E':
            if bit == '1':
                self.state = 'O'
                return '1'  # Odd count reached -> output 1
            else:
                return '0'  # Still even -> output 0

        elif self.state == 'O':
            if bit == '1':
                self.state = 'E'
                return '0'  # Back to even count -> output 0
            else:
                return '1'  # Still odd -> output 1

    def run(self, input_string: str):
        output_bits = []
        state_history = [self.state]

        for bit in input_string:
            out = self.process_bit(bit)
            output_bits.append(out)
            state_history.append(self.state)

        return "".join(output_bits), state_history


# --- Demonstration ---
if __name__ == "__main__":
    input_str = "10110"
    machine = ParityDetectorMealy()
    output_str, history = machine.run(input_str)

    print("=== ODD PARITY MEALY MACHINE ===")
    print(f"Input : {input_str}")
    print(f"Output: {output_str}")
    print(f"States: {' -> '.join(history)}")