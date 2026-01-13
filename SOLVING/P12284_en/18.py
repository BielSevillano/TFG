
import sys
from collections import Counter
import heapq

def solve():
    """
    This function reads input cases and processes them until EOF.
    """
    while True:
        line = sys.stdin.readline()
        if not line:
            break

        try:
            n, k = map(int, line.split())
        except (ValueError, IndexError):
            # Handles potential empty lines between cases
            continue

        # Read the n words for the current case
        words = [sys.stdin.readline().strip() for _ in range(n)]

        # Count the frequency of each word
        counts = Counter(words)

        # The sorting criteria are:
        # 1. Frequency in descending order.
        # 2. In case of a tie, word in lexicographical (alphabetical) ascending order.
        #
        # A key tuple `(-count, word)` achieves this sorting. A smaller tuple
        # value represents a more frequent or alphabetically smaller word.
        #
        # `heapq.nsmallest(k, iterable, key)` is an efficient way to find the k
        # items with the smallest key values. It's more efficient than sorting
        # the entire list of unique words, especially when k is much smaller
        # than the number of unique words. `nsmallest` also returns the items
        # sorted according to the key.
        
        top_k_items = heapq.nsmallest(k, counts.items(), key=lambda item: (-item[1], item[0]))

        # Print the word from each of the top k items
        for word, _ in top_k_items:
            print(word)

        print('----------')

solve()
