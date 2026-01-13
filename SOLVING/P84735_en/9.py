
import sys

def solve():
    """
    Reads pairs of natural numbers a and b from standard input and for each pair,
    prints the smallest natural number x such that x >= a and x is a multiple of b.
    """
    case_number = 1
    for line in sys.stdin:
        # Strip potential whitespace and skip empty lines
        line = line.strip()
        if not line:
            continue

        try:
            a, b = map(int, line.split())

            # The problem is to find the smallest multiple of b that is >= a.
            # This is equivalent to finding ceiling(a / b) and then multiplying by b.
            #
            # For non-negative integers a and b (with b > 0), integer ceiling
            # division ceil(a / b) can be calculated as (a + b - 1) // b.
            #
            # Example 1: a = 10, b = 3
            # a / b = 3.33...
            # ceil(a / b) = 4
            # Smallest multiple is 4 * 3 = 12.
            # Formula: (10 + 3 - 1) // 3 = 12 // 3 = 4. Result: 4 * 3 = 12. Correct.
            #
            # Example 2: a = 12, b = 3
            # a / b = 4.0
            # ceil(a / b) = 4
            # Smallest multiple is 4 * 3 = 12.
            # Formula: (12 + 3 - 1) // 3 = 14 // 3 = 4. Result: 4 * 3 = 12. Correct.
            
            # Since b >= 1, we don't need to check for division by zero.
            if a == 0:
                result = 0
            else:
                # The formula (a + b - 1) // b finds the multiplier.
                # It effectively rounds up the division a / b.
                # However, for a=0, we need the result to be 0.
                # (0 + b - 1)//b * b might give 0 or b depending on b.
                # e.g., b=1 -> (0)//1*1 = 0.
                # e.g., b>1 -> (b-1)//b * b = 0*b = 0.
                # So the single formula actually works for a=0 as well.
                # The if/else is more explicit but not strictly necessary.

                result = ((a + b - 1) // b) * b

            print(f"Case #{case_number}: {result}")
            case_number += 1
        except (ValueError, IndexError):
            # This handles malformed lines (e.g., non-integers, wrong number of values)
            # and gracefully stops the program.
            break

solve()
