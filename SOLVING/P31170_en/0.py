
import sys

def solve():
    """
    Reads a number from stdin and prints its multiplication table.
    """
    try:
        line = sys.stdin.readline()
        if not line:
            return
        
        n = int(line)
        
        for i in range(1, 11):
            result = n * i
            print(f"{n} x {i} = {result}")

    except (ValueError, IndexError):
        # As per problem constraints, input will be a valid natural number.
        # This is for robustness in a general case, but not strictly
        # required by the problem statement.
        pass

# The problem implies a single execution for a single number.
# If multiple test cases were possible on the same input stream,
# a loop would be needed, e.g., while True: solve().
# For a typical online judge setup, this single call is correct.
solve()
