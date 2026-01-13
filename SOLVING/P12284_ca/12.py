
import sys
from collections import Counter

# Read all whitespace-separated tokens from stdin.
# This is efficient and handles various input layouts (e.g., words on same or different lines).
try:
    tokens = sys.stdin.read().split()
except IOError:
    tokens = []

# A pointer to the current position in the token list.
idx = 0

# Process the tokens stream case by case.
while idx < len(tokens):
    # Each case starts with n and k.
    try:
        n = int(tokens[idx])
        k = int(tokens[idx + 1])
        idx += 2
    except (ValueError, IndexError):
        # This could happen with malformed input at the very end.
        # Safely terminate the loop.
        break

    # Get the n words for the current case.
    # We slice the list of tokens.
    words = tokens[idx : idx + n]
    idx += n

    # Use collections.Counter for efficient frequency counting.
    counts = Counter(words)

    # Sort the words. The primary key is frequency (descending),
    # and the secondary key is the word itself (lexicographically ascending).
    # A lambda function with a tuple is a concise way to define this multi-level sort key.
    # item[1] is the count, item[0] is the word.
    # Negating the count achieves descending order for the primary key.
    sorted_words = sorted(counts.items(), key=lambda item: (-item[1], item[0]))

    # Print the top k most frequent words.
    # The problem guarantees that 1 <= k <= number of distinct words.
    for i in range(k):
        print(sorted_words[i][0])

    # Print the separator line after each case.
    print("----------")
