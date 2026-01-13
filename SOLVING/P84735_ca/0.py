
import sys

def solve():
    """
    Reads pairs of numbers a, b from standard input and for each pair,
    prints the smallest natural number x such that x >= a and x is a multiple of b.
    """
    try:
        # Read the entire input and split it into a list of strings (numbers).
        # This is an efficient way to handle various input formats (e.g., numbers on
        # the same line or different lines) in competitive programming.
        tokens = sys.stdin.read().split()
        
        # If the input is empty, do nothing.
        if not tokens:
            return

        # Create an iterator over the tokens for easy consumption.
        token_iterator = iter(tokens)
        
        case_number = 1
        
        # Loop indefinitely; the loop will be broken by an exception when input ends.
        while True:
            # Read the next two tokens and convert them to integers.
            # This will raise StopIteration if the iterator is exhausted.
            a = int(next(token_iterator))
            b = int(next(token_iterator))

            # The problem guarantees b >= 1, so no risk of division by zero.
            
            # Check if 'a' is already a multiple of 'b'.
            if a % b == 0:
                # If it is, 'a' is the smallest multiple of 'b' that is >= 'a'.
                result = a
            else:
                # If 'a' is not a multiple of 'b', the smallest multiple of 'b'
                # greater than 'a' is the next multiple after the one just before 'a'.
                # The integer division `a // b` gives the quotient. The next multiple
                # is found by multiplying `b` by `quotient + 1`.
                result = (a // b + 1) * b

            # Print the result in the required format.
            print(f"Case #{case_number}: {result}")
            
            # Increment the case counter for the next pair.
            case_number += 1

    except StopIteration:
        # This exception is expected and occurs when the token_iterator has no more
        # items, indicating the end of the input. We simply pass to exit gracefully.
        pass
    except ValueError:
        # This would catch errors if a token is not a valid integer.
        # The problem statement implies valid natural numbers, but this makes
        # the code more robust.
        pass

# Execute the main logic.
solve()
