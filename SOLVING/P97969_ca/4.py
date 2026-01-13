
import sys

# Read all input until end-of-file
full_input = sys.stdin.read()

# The sequence is defined as all characters before the first period
# The split method with a maxsplit of 1 is an efficient way to get this part
sequence = full_input.split('.', 1)[0]

# Use the built-in count method to find the number of 'a's
a_count = sequence.count('a')

# Print the final count
print(a_count)
