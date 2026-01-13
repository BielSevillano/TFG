
import sys

def solve():
    """
    Reads pairs of numbers a, b from standard input and for each pair,
    prints the smallest multiple of b that is greater than or equal to a.
    """
    case_number = 1
    for line in sys.stdin:
        # Split the line into parts. Handles various whitespace.
        parts = line.split()
        
        # If the line is empty or contains only whitespace, skip it.
        if not parts:
            continue

        try:
            a, b = map(int, parts)
            
            # Since b is a natural number >= 1, no need to check for b=0.
            
            remainder = a % b
            
            if remainder == 0:
                # If a is already a multiple of b, it's the smallest >= a.
                result = a
            else:
                # Otherwise, we need to find the next multiple.
                # This is a plus the difference needed to reach the next multiple.
                result = a + b - remainder
            
            print(f"Case #{case_number}: {result}")
            case_number += 1
            
        except (ValueError, IndexError):
            # If a line is malformed (e.g., not two numbers),
            # we can either ignore it or stop. Ignoring is more robust
            # for inputs with accidental blank lines.
            continue

solve()
