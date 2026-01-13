
import sys

def solve():
    """
    Reads pairs of numbers a, b from stdin and for each pair,
    prints the smallest multiple of b that is greater than or equal to a.
    """
    case_number = 1
    for line in sys.stdin:
        # Strip whitespace from the line and check if it's empty.
        line = line.strip()
        if not line:
            continue

        try:
            # Parse the two numbers from the line.
            a, b = map(int, line.split())

            # The problem guarantees b >= 1.
            # We are looking for the smallest integer x such that:
            # 1. x >= a
            # 2. x is a multiple of b.
            #
            # This is equivalent to finding ceil(a / b) and multiplying by b.
            #
            # For non-negative integer a and positive integer b,
            # ceil(a / b) can be calculated using integer arithmetic as (a + b - 1) // b.
            
            result = ((a + b - 1) // b) * b

            # Print the output in the required format.
            print(f"Case #{case_number}: {result}")

            # Increment the case number for the next input pair.
            case_number += 1
        except (ValueError, IndexError):
            # This handles lines that do not contain exactly two integers.
            # In a typical contest setting with well-formed input, this might
            # not be strictly necessary, but it makes the script more robust.
            pass

if __name__ == "__main__":
    solve()
