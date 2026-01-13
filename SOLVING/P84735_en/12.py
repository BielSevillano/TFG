
import sys

def solve():
    """
    Reads pairs of numbers a, b from stdin and for each pair,
    prints the smallest multiple of b that is greater than or equal to a.
    """
    case_num = 1
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue

        try:
            a, b = map(int, line.split())
            
            # The smallest multiple of b >= a can be calculated using the
            # ceiling of a/b.
            # x = ceil(a/b) * b
            # In integer arithmetic, for non-negative a and positive b,
            # ceil(a/b) can be calculated as (a + b - 1) // b.
            # This formula works even for a = 0.
            
            if b == 0:
                # This case is excluded by the problem statement (b >= 1),
                # but good practice to handle.
                # The behavior is undefined, so we can skip or handle as an error.
                continue

            # If a is 0, the smallest multiple of b >= 0 is 0.
            # The formula ((0 + b - 1) // b) * b correctly evaluates to 0.
            
            result = ((a + b - 1) // b) * b

            print(f"Case #{case_num}: {result}")
            case_num += 1

        except (ValueError, IndexError):
            # This handles lines that don't contain two valid integers
            # or are otherwise malformed.
            continue

if __name__ == "__main__":
    solve()
