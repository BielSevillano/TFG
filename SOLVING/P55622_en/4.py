
import sys

# The problem states that the input is a single natural number.
# We read from standard input. `input()` reads one line and strips the trailing newline.
# We convert this line to an integer using `int()`. This correctly handles
# potential leading/trailing whitespace and interprets numbers with leading
# zeros (e.g., "007") as their numerical value (7).
try:
    n = int(input())
    
    # We then convert the integer back to its canonical string representation.
    # For example, the integer 123 becomes the string "123".
    # The integer 0 becomes the string "0".
    s = str(n)
    
    # The number of digits is the length of this canonical string.
    print(len(s))

except (IOError, EOFError):
    # This handles cases where the input stream is empty or closed,
    # ensuring the program terminates gracefully as required.
    pass
