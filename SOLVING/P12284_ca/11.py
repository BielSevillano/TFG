
import sys
from collections import Counter

def solve():
    """
    Reads test cases and for each, finds the k most frequent words.
    """
    # Process input until End-Of-File is reached
    while True:
        line = sys.stdin.readline()
        if not line:
            break

        # Attempt to parse n and k. If a line is empty or malformed,
        # it will be skipped, which is robust for varied input formats.
        try:
            n, k = map(int, line.split())
        except ValueError:
            continue

        # Read the n words for the current test case using a list comprehension
        words = [sys.stdin.readline().strip() for _ in range(n)]

        # Use collections.Counter for an efficient O(n) frequency count
        word_counts = Counter(words)

        # Sort the items from the counter.
        # The key for sorting is a tuple: (-frequency, word).
        # - The negative frequency ensures sorting in descending order of counts.
        # - The word itself is the secondary key, ensuring lexicographical
        #   (alphabetical) order for words with the same frequency.
        sorted_items = sorted(word_counts.items(), key=lambda item: (-item[1], item[0]))

        # Print the first k words from the sorted list
        for i in range(k):
            print(sorted_items[i][0])

        # Print the required separator line
        print("----------")

if __name__ == "__main__":
    solve()
