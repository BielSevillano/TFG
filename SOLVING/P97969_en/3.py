
import sys

# Read the entire standard input into a single string.
# This approach is efficient for inputs that can fit into memory.
input_text = sys.stdin.read()

# The sequence of characters is defined to end at the first period.
# We split the input string by the period just once and take the first part.
# This correctly isolates the sequence we need to analyze.
sequence = input_text.split('.', 1)[0]

# Use the highly optimized built-in string method `count()`
# to find the number of occurrences of the letter 'a'.
a_count = sequence.count('a')

# Print the final count to standard output.
print(a_count)
