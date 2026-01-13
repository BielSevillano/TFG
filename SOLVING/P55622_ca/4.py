
import sys

try:
    # Read the number as a string from the input.
    # input() reads a line, strips the trailing newline, and returns it.
    n_str = input()
    
    # The number of digits is the length of its string representation.
    # We print the length of the string.
    print(len(n_str))

except EOFError:
    # This block handles the case where the input stream is empty,
    # preventing an error. The program will simply exit gracefully.
    pass
