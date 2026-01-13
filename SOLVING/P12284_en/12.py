
import sys
from collections import Counter

# Read all whitespace-separated tokens from standard input at once.
# This approach is efficient and robust against various input formatting
# like multiple words per line or extra newlines between cases.
try:
    tokens = sys.stdin.read().split()
except IOError:
    tokens = []

# An index to keep track of our current position in the list of tokens.
idx = 0

# Loop through the tokens until all have been processed.
while idx < len(tokens):
    # Each test case begins with two integers, n and k.
    try:
        n = int(tokens[idx])
        k = int(tokens[idx + 1])
        idx += 2
    except (ValueError, IndexError):
        # This handles cases where the input might not be perfectly formed
        # at the very end, e.g., trailing whitespace.
        break

    # The next n tokens are the words for the current test case.
    # We slice the list to get them.
    if idx + n > len(tokens):
        # In case of malformed input where there are not enough words.
        break
        
    words = tokens[idx : idx + n]
    idx += n

    # Use collections.Counter to efficiently count the frequency of each word.
    counts = Counter(words)

    # Sort the unique words. The sorting criteria are:
    # 1. Primary key: Frequency in descending order.
    # 2. Secondary key (for ties): The word itself in lexicographical order.
    # We achieve this by providing a tuple `(-frequency, word)` as the sort key.
    # The negative sign on the frequency effectively sorts it in descending order.
    sorted_words = sorted(counts.keys(), key=lambda word: (-counts[word], word))

    # Print the top k words as required by the problem.
    # The problem guarantees that k will be at least 1 and no more than
    # the number of unique words, so we don't need to check bounds.
    for i in range(k):
        print(sorted_words[i])
    
    # Print the separator line at the end of each test case.
    print('----------')
