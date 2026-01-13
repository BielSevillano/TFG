
import sys

# Read the entire input stream at once.
# This is efficient for the typical size of inputs in competitive programming.
full_input = sys.stdin.read()

# The problem states the sequence ends with a period '.'.
# We can find the first occurrence of '.' and consider the sequence to be everything before it.
# The split() method is a clean way to do this.
# By specifying `1` as the second argument, we ensure it only splits at the first period.
# We then take the first part of the split result, which is the sequence we need to analyze.
sequence_before_period = full_input.split('.', 1)[0]

# Use the highly optimized built-in string method count() to find the number of 'a's.
a_count = sequence_before_period.count('a')

# Print the final count, followed by a newline, which is the standard output format.
print(a_count)
