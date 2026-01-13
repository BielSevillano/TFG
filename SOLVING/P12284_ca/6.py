
import sys
from collections import Counter

def solve():
    """
    Reads all test cases from stdin and processes them.
    """
    # Create a generator that yields all whitespace-separated tokens from stdin.
    # This is memory-efficient as it doesn't read the entire input at once.
    tokens = (word for line in sys.stdin for word in line.split())

    # Loop to handle each test case.
    while True:
        try:
            # Read n and k for the current case.
            n = int(next(tokens))
            k = int(next(tokens))
        except StopIteration:
            # If the generator is exhausted, there are no more cases.
            break
        
        # Read the n words for this case.
        words = [next(tokens) for _ in range(n)]

        # Use collections.Counter to efficiently count word frequencies.
        counts = Counter(words)

        # Sort the items (word, count) from the counter.
        # The primary sorting key is the frequency (in descending order).
        # The secondary sorting key (for ties) is the word (in ascending lexicographical order).
        # This is achieved by sorting on a tuple `(-count, word)`.
        sorted_items = sorted(counts.items(), key=lambda item: (-item[1], item[0]))

        # Print the top k words from the sorted list.
        for i in range(k):
            print(sorted_items[i][0])
        
        # Print the required separator after each case.
        print("----------")

solve()
