
import sys
from collections import Counter

def solve():
    """
    Reads all test cases from stdin and solves the most frequent words problem for each.
    """
    # Read all whitespace-separated tokens from stdin at once.
    # This is efficient and handles various input formatting (words on the same line or different lines).
    try:
        tokens = sys.stdin.read().split()
    except Exception:
        return

    # If there's no input, do nothing.
    if not tokens:
        return

    # Use an index to walk through the token list.
    idx = 0
    while idx < len(tokens):
        # Every case starts with n and k. We assume the input is well-formed.
        try:
            n = int(tokens[idx])
            k = int(tokens[idx + 1])
        except (ValueError, IndexError):
            # Stop if the input is malformed (e.g., cannot parse n, k).
            break
        
        # Move index past n and k.
        idx += 2

        # Check if there are enough words for the current case.
        if idx + n > len(tokens):
            break

        # Get the n words for the current case.
        words = tokens[idx : idx + n]
        
        # Move index past the words for the next case.
        idx += n

        # 1. Count word frequencies using collections.Counter.
        word_counts = Counter(words)
        
        # 2. Sort the items (word, count) based on the specified criteria:
        #    - Primary key: frequency (descending)
        #    - Secondary key: word (lexicographically ascending)
        # The key for sorting will be a tuple: (-count, word).
        sorted_items = sorted(word_counts.items(), key=lambda item: (-item[1], item[0]))
        
        # 3. Print the top k words.
        # The problem guarantees that k is valid, so we don't need to check
        # if len(sorted_items) is less than k.
        for i in range(k):
            print(sorted_items[i][0])
        
        # 4. Print the separator line.
        print("----------")

solve()
