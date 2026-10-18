class MealyMachine1sComplement:
    def __init__(self):
        # Initial state is 'A'
        self.current_state = 'A'

    def process_bit(self, bit: str) -> str:
        """
        Processes a single input bit ('0' or '1') and returns the output bit.
        In a 1's complement Mealy machine:
        - Input '0' outputs '1'
        - Input '1' outputs '0'
        State remains 'A'.
        """
        if bit == '0':
            return '1'
        elif bit == '1':
            return '0'
        else:
            raise ValueError(f"Invalid input bit: {bit}. Must be '0' or '1'.")

    def process_string(self, input_string: str) -> tuple[str, list[str]]:
        """
        Processes a binary string and returns:
        1. The output string (1's complement)
        2. The state trace (sequence of states)
        """
        output_bits = []
        state_trace = [self.current_state]

        for bit in input_string:
            out_bit = self.process_bit(bit)
            output_bits.append(out_bit)
            # Machine stays in state 'A' for all inputs
            state_trace.append(self.current_state)

        return "".join(output_bits), state_trace


# --- Demonstration matching the handwritten notes ---
if __name__ == "__main__":
    input_str = "1010"
    
    mealy = MealyMachine1sComplement()
    output_str, states = mealy.process_string(input_str)

    print("=== FINITE AUTOMATA WITH OUTPUTS: MEALY MACHINE ===")
    print(f"Input String  : {input_str}")
    print(f"Output String : {output_str}")
    print(f"State Trace   : {' -> '.join(states)}")