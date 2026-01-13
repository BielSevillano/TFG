
import sys

# Read the entire input stream until the end-of-file.
# This is generally more efficient in Python than reading character by character.
full_input = sys.stdin.read()

# The problem states the sequence is terminated by a period.
# We split the string at the first occurrence of the period and take the
# first part (the content before the period). The '1' argument ensures
# that we only split on the first period found.
sequence_before_period = full_input.split('.', 1)[0]

# Use the highly optimized built-in string method 'count' to find the
# number of occurrences of the character 'a'.
count = sequence_before_period.count('a')

# Print the final count to the standard output.
print(count)
