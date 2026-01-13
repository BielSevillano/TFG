
import sys

def main():
    """
    Main function to solve the problem. It reads pairs of natural numbers a and b
    from standard input and, for each pair, calculates and prints the smallest
    natural number x such that x is greater than or equal to a and is a multiple of b.
    """
    case_number = 1
    for line in sys.stdin:
        # Strip the line to handle potential leading/trailing whitespace.
        line = line.strip()
        
        # If the line is empty, skip it. This handles potential blank lines in the input.
        if not line:
            continue
        
        # Attempt to parse two integers from the line.
        # This structure is robust against malformed lines.
        try:
            a, b = map(int, line.split())
        except (ValueError, IndexError):
            continue
            
        # The problem statement guarantees b >= 1.
        
        # If a is already a multiple of b, then a is the smallest multiple of b
        # that is greater than or equal to a.
        if a % b == 0:
            result = a
        else:
            # If a is not a multiple of b, we need to find the next multiple.
            # The integer division `a // b` gives the quotient q.
            # The multiple of b just before or at a is `q * b`.
            # The next multiple of b will be `(q + 1) * b`. This is guaranteed
            # to be greater than or equal to a.
            result = (a // b + 1) * b
            
        # Print the result in the specified format for each case.
        print(f"Case #{case_number}: {result}")
        
        # Increment the case counter for the next input pair.
        case_number += 1

if __name__ == "__main__":
    main()
