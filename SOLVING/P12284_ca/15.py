
import sys
from collections import Counter

def solve():
    """
    Reads all input, processes each case, and prints the results.
    This approach reads the entire input into memory first, which is
    fast for typical competitive programming input sizes.
    """
    # Read the entire input and split it into a list of tokens (words/numbers).
    tokens = sys.stdin.read().split()

    # If the input is empty, do nothing.
    if not tokens:
        return

    # Use an index to iterate through the tokens.
    idx = 0
    while idx < len(tokens):
        # Each case starts with n and k.
        n = int(tokens[idx])
        k = int(tokens[idx + 1])
        idx += 2

        # The next n tokens are the words for this case.
        words = tokens[idx : idx + n]
        idx += n

        # Use collections.Counter to count word frequencies efficiently.
        counts = Counter(words)

        # Sort the items (word, count) from the counter.
        # The primary sorting key is the frequency (in descending order),
        # achieved by using the negative of the count (-item[1]).
        # The secondary sorting key is the word itself (in ascending
        # lexicographical order), which is the default tie-breaker for tuples.
        sorted_items = sorted(counts.items(), key=lambda item: (-item[1], item[0]))

        # Print the first k words from the sorted list.
        for i in range(k):
            print(sorted_items[i][0])
        
        # Print the required separator line after each case.
        print("----------")

solve()
