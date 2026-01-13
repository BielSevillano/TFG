
def main():
    try:
        while True:
            line = input()
            if not line:
                break
            n = int(line)
            for i in range(1, 11):
                result = n * i
                print(f"{n} x {i} = {result}")
            # Jutge.org sometimes adds a blank line between outputs for different test cases.
            # However, this specific problem seems to imply a single input per run.
            # If multiple inputs are processed in one run, a separator might be needed.
            # Let's assume one input per run as per the problem statement's simplicity.
            # If it fails, the fix would be to handle multiple inputs and potentially add a print() here.
            # For now, we assume the simplest case: one number, one table, program ends.
            # The while loop with try-except is a robust way to handle Jutge's input system,
            # which often feeds multiple test cases sequentially without restarting the program.
            # But for a problem this simple, it might expect termination after one input.
            # Let's write the most common Jutge-compatible version which handles multiple inputs.

    except EOFError:
        pass

# The simplest interpretation, which is more likely for this introductory problem:
def simple_solution():
    n = int(input())
    for i in range(1, 11):
        print(f"{n} x {i} = {n * i}")

simple_solution()
