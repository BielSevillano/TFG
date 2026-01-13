
import sys

# Read the entire input stream up to the end-of-file.
# Then, split the resulting string at the first occurrence of a period.
# The '1' in split ensures we only split once, handling cases with multiple periods.
# We take the first part of the split result, which is the sequence before the period.
sequence = sys.stdin.read().split('.', 1)[0]

# Use the built-in string method 'count' to efficiently count the number of 'a's.
# Finally, print the result.
print(sequence.count('a'))
