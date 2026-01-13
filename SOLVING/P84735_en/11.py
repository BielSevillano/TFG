
import sys

def solve_smallest_multiple():
    """
    Reads pairs of natural numbers a and b from standard input and for each
    pair, prints the smallest natural number x such that x >= a and x is a
    multiple of b.
    """
    case_number = 1
    for line in sys.stdin:
        try:
            # Attempt to read and parse the two integers from the line.
            # Stripping the line is a good practice to handle various newline formats.
            parts = line.strip().split()
            if not parts:
                continue  # Skip empty lines
            a, b = map(int, parts)

            # Given a and b, find the smallest multiple of b that is >= a.
            # Let r be the remainder of a divided by b.
            # a = q*b + r, where q is the quotient.
            
            remainder = a % b
            
            # If the remainder is 0, 'a' is already a multiple of b.
            # Since we need the smallest multiple >= a, 'a' is the answer.
            if remainder == 0:
                result = a
            else:
                # If 'a' is not a multiple, the previous multiple of b is a - remainder.
                # The next multiple of b is (a - remainder) + b.
                # This can also be seen as adding the "gap" to 'a' to reach
                # the next multiple, which is b - remainder.
                result = a + (b - remainder)
            
            # Print the output in the required format for each case.
            print(f"Case #{case_number}: {result}")
            case_number += 1
            
        except (ValueError, IndexError):
            # This block will be reached if a line is malformed (e.g., not two numbers)
            # or if an empty line at the end of input causes split() to return an
            # empty list, leading to an unpacking error. This gracefully ends the loop.
            break

solve_smallest_multiple()
