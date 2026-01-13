
import sys
from collections import Counter

def solve():
    """
    Reads all input, processes test cases, and prints the results.
    """
    # Read all whitespace-separated tokens from stdin at once.
    # This is efficient and robust for typical competitive programming input formats.
    try:
        tokens = sys.stdin.read().split()
    except Exception:
        return

    if not tokens:
        return

    # Use an index to iterate through the stream of tokens.
    idx = 0
    while idx < len(tokens):
        # Each test case starts with n and k.
        try:
            n = int(tokens[idx])
            k = int(tokens[idx + 1])
        except (ValueError, IndexError):
            # Stop if n and k cannot be parsed, indicating end of valid input.
            break

        idx += 2
        
        # Check if there are enough words remaining for this test case.
        if idx + n > len(tokens):
            break

        # Get the n words for the current case.
        words = tokens[idx : idx + n]
        idx += n

        # Count word frequencies efficiently.
        counts = Counter(words)

        # Sort the words. The primary key is frequency (descending),
        # and the secondary key is the word itself (lexicographically ascending).
        # We sort the (word, count) items from the Counter.
        sorted_word_freq = sorted(counts.items(), key=lambda item: (-item[1], item[0]))

        # Print the top k words as required.
        for i in range(k):
            print(sorted_word_freq[i][0])
        
        # Print the separator line.
        print("----------")

solve()
