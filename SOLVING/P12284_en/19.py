
import sys
from collections import Counter

try:
    # Read all input at once and split into tokens. This approach is efficient
    # and robust against variations in whitespace (spaces vs. newlines).
    tokens = sys.stdin.read().split()
    
    # Create an iterator to consume the tokens sequentially.
    it = iter(tokens)

    # Process test cases until the iterator is exhausted.
    while True:
        # Read n and k for the current test case.
        # This will raise StopIteration when the input ends.
        n = int(next(it))
        k = int(next(it))
        
        # Read the n words for this case.
        words = [next(it) for _ in range(n)]
        
        # Use collections.Counter to efficiently count word frequencies.
        counts = Counter(words)
        
        # Sort the (word, count) pairs. The sorting key is a tuple
        # to handle multiple criteria:
        # 1. Primary key: frequency, in descending order (hence the negation).
        # 2. Secondary key: word, in lexicographical (ascending) order.
        sorted_items = sorted(counts.items(), key=lambda item: (-item[1], item[0]))
        
        # Print the top k words from the sorted list.
        for i in range(k):
            print(sorted_items[i][0])
            
        # Print the separator line at the end of the case.
        print("----------")

except (StopIteration, ValueError, IndexError):
    # This block catches exceptions that signal the end of input or a
    # malformed final case, allowing the program to terminate gracefully.
    # - StopIteration: Raised by next() on an exhausted iterator (EOF).
    # - ValueError: Raised if int() conversion fails.
    # - IndexError: A safeguard, though unlikely given the problem constraints.
    pass
