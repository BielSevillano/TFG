
import sys

def main():
    """
    Reads pairs of natural numbers a and b, and for each pair,
    prints the smallest natural number that is greater than or
    equal to a and also a multiple of b.
    """
    case_num = 1
    for line in sys.stdin:
        try:
            a, b = map(int, line.split())
        except (ValueError, IndexError):
            # Skip empty or malformed lines
            continue

        # To find the smallest multiple of b that is >= a, we can use
        # the concept of ceiling division. We are looking for ceil(a/b) * b.
        # In integer arithmetic, for non-negative a and positive b,
        # ceil(a/b) can be calculated as (a + b - 1) // b.
        
        # If a is already a multiple of b, a % b == 0.
        # The result should be a.
        # Let's test the formula: a = k*b
        # ((k*b + b - 1) // b) * b -> k*b
        #
        # If a is not a multiple of b, a % b != 0.
        # The result should be the next multiple of b.
        # (a // b + 1) * b
        # Let's test the formula: a = k*b + r, with 0 < r < b
        # ((k*b + r + b - 1) // b) * b
        # Since 1 <= r < b, we have k*b + b <= k*b + r + b - 1 < k*b + 2b - 1
        # So (k*b + r + b - 1) // b is k+1. The result is (k+1)*b.
        # The formula works for all cases where a >= 0 and b >= 1.
        
        # The most straightforward and readable implementation is often a simple check.
        if a % b == 0:
            result = a
        else:
            result = (a // b + 1) * b

        print(f"Case #{case_num}: {result}")
        case_num += 1

if __name__ == "__main__":
    main()
