
import sys

def main():
    """
    Reads pairs of natural numbers a and b from standard input and for each pair,
    finds the smallest natural number x such that x >= a and x is a multiple of b.
    """
    case_num = 1
    for line in sys.stdin:
        # Strip whitespace and check if the line is empty
        line = line.strip()
        if not line:
            continue

        try:
            a, b = map(int, line.split())
        except (ValueError, IndexError):
            # If the line is malformed (e.g., not two numbers), skip it or stop.
            # In this context, we can just continue to the next line.
            continue
        
        # Calculate the smallest multiple of b that is greater than or equal to a.
        # If a is already a multiple of b, the answer is a itself.
        # The remainder of a divided by b is a % b.
        remainder = a % b
        
        if remainder == 0:
            result = a
        else:
            # If a is not a multiple, we need to find the next one.
            # a - remainder gives the largest multiple of b that is smaller than a.
            # Adding b to this gives the smallest multiple of b that is greater than a.
            result = a - remainder + b
            
        print(f"Case #{case_num}: {result}")
        case_num += 1

if __name__ == "__main__":
    main()
