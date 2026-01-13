
import sys

# Read all text from standard input until the end-of-file.
# The problem statement implies a single block of text.
full_text = sys.stdin.read()

# The sequence is defined as all characters up to the first period.
# We can use split('.', 1) to break the text at the first period.
# The '1' ensures we only split once, which is slightly more efficient.
# We then take the first part of the result (index [0]).
# This robustly handles cases where there is no period (the whole string is taken)
# or the period is the first character (an empty string is taken).
sequence = full_text.split('.', 1)[0]

# Use the built-in string method count() to count occurrences of 'a'.
# This is highly optimized.
a_count = sequence.count('a')

# Print the final count.
print(a_count)
