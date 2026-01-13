
import sys

# The problem states that the input is a single natural number.
# We read the entire input, which might span multiple lines if the number is very large,
# but for typical competitive programming scenarios, a number is given on a single line.
# A robust way is to read from the standard input stream.
# We can read a single line using input().
try:
    s = input()
    # The input might have leading zeros (e.g., "007").
    # To count the digits of the actual number, we first convert the string to an integer.
    # This automatically handles leading zeros and any surrounding whitespace.
    # For example, int("007") results in the integer 7.
    n = int(s)
    # Then, we convert the integer back to a string to get its canonical representation.
    # For example, str(7) results in the string "7".
    # The length of this canonical string is the number of digits.
    # This also correctly handles the edge case of n=0, where str(0) is "0" and its length is 1.
    print(len(str(n)))
except (IOError, ValueError):
    # This handles cases where input is empty or not a valid number,
    # though the problem statement guarantees a natural number.
    # In a real-world scenario, robust error handling is good practice.
    # For this problem, this block might not be strictly necessary.
    pass
