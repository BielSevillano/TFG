
import sys
from collections import Counter

try:
    # Read all input at once and split by whitespace to get a list of tokens.
    # This is efficient for typical competitive programming input sizes.
    tokens = iter(sys.stdin.read().split())
    
    # Process test cases in a loop until the input is exhausted.
    while True:
        # Each test case begins with two integers, n and k.
        n = int(next(tokens))
        k = int(next(tokens))
        
        # Read the n words for the current test case.
        words = [next(tokens) for _ in range(n)]
        
        # Use collections.Counter to efficiently count the frequency of each word.
        counts = Counter(words)
        
        # Convert the counter's items to a list and sort it.
        # The sorting key is a tuple:
        # 1. -item[1]: The negative of the frequency, to sort in descending order of frequency.
        # 2. item[0]: The word itself, to sort in ascending lexicographical order for ties.
        sorted_items = sorted(counts.items(), key=lambda item: (-item[1], item[0]))
        
        # Print the first k words from the sorted list.
        for i in range(k):
            print(sorted_items[i][0])
            
        # Print the required separator line after each test case's output.
        print("----------")

except (StopIteration, ValueError):
    # The loop terminates when `next(tokens)` raises a StopIteration (end of input)
    # or a ValueError (e.g., trying to parse an empty string from trailing whitespace).
    # In either case, the program should end gracefully.
    pass
