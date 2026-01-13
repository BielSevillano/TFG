
import sys

case_num = 1
for line in sys.stdin:
    # It is good practice to strip the line, especially to handle the final empty line
    # that might exist in some test files, or lines with only whitespace.
    stripped_line = line.strip()
    if not stripped_line:
        continue
    
    # Split the line and convert the parts to integers.
    try:
        a, b = map(int, stripped_line.split())
    except (ValueError, IndexError):
        # In case a line is malformed, skip it.
        continue

    # The logic is based on whether 'a' is already a multiple of 'b'.
    # If a is a multiple of b (a % b == 0), then 'a' itself is the smallest
    # natural number that is >= a and a multiple of b.
    if a % b == 0:
        result = a
    else:
        # If 'a' is not a multiple of 'b', we need to find the next multiple.
        # Integer division a // b gives the quotient.
        # (a // b) * b is the largest multiple of b that is less than or equal to a.
        # So, the next multiple of b (the smallest one >= a) is (a // b + 1) * b.
        result = (a // b + 1) * b
        
    # Print the output in the specified format for each case.
    print(f"Case #{case_num}: {result}")
    
    # Increment the case number for the next pair of inputs.
    case_num += 1
