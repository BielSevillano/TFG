
import sys

# Read the entire input stream from standard input.
# The problem defines the sequence as all characters up to the first period.
# We can isolate this sequence by reading everything, splitting the string
# at the first occurrence of '.', and taking the first part.
# The split method with maxsplit=1 is efficient for this purpose.
sequence = sys.stdin.read().split('.', 1)[0]

# Use the built-in string method count() to find the number of 'a's.
a_count = sequence.count('a')

# Print the final result to standard output.
print(a_count)
