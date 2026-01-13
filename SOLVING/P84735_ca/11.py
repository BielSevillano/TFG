
import sys

try:
    # This I/O method reads all input at once, splits by any whitespace,
    # and creates an iterator of integers. It is generally fast and robust
    # to variations in input formatting (e.g., numbers on one line vs. many).
    it = iter(map(int, sys.stdin.read().split()))
    
    case_num = 1
    
    # Process the numbers in pairs (a, b) until the input is exhausted.
    while True:
        a = next(it)
        b = next(it)
        
        # We need the smallest multiple of b that is greater than or equal to a.
        
        # If a is already a multiple of b, it is the answer itself.
        if a % b == 0:
            result = a
        else:
            # Otherwise, we find the next multiple of b.
            # (a // b) * b gives the largest multiple of b less than a.
            # The next multiple is therefore ((a // b) + 1) * b.
            result = (a // b + 1) * b
        
        # Print the output in the required format.
        print(f"Case #{case_num}: {result}")
        
        case_num += 1

except StopIteration:
    # The `next(it)` call will raise StopIteration when there are no more
    # numbers in the input. This is the normal and expected way to end
    # the loop, so we simply pass to allow the program to terminate gracefully.
    pass
