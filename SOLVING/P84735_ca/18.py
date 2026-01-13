
import sys

def main():
    """
    Reads pairs of natural numbers a and b from standard input,
    and for each pair, calculates and prints the smallest natural number
    that is greater than or equal to a and also a multiple of b.
    """
    case_number = 1
    for line in sys.stdin:
        # Strip leading/trailing whitespace and check for empty lines
        line = line.strip()
        if not line:
            continue

        try:
            a, b = map(int, line.split())
        except (ValueError, IndexError):
            # Skip malformed lines
            continue
        
        # The problem statement guarantees b >= 1.
        
        # Calculate the remainder of a divided by b.
        remainder = a % b
        
        if remainder == 0:
            # If a is already a multiple of b, it is the smallest
            # multiple of b that is greater than or equal to a.
            result = a
        else:
            # If a is not a multiple of b, the next multiple of b is needed.
            # a - remainder is the largest multiple of b less than a.
            # Adding b to it gives the smallest multiple of b greater than a.
            result = a - remainder + b
            
        print(f"Case #{case_number}: {result}")
        case_number += 1

if __name__ == "__main__":
    main()
