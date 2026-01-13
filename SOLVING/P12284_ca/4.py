
import sys
from collections import Counter

def solve():
    """
    Reads all test cases from stdin and processes them.
    This approach uses a generator to read a flat stream of tokens,
    which is robust against whitespace variations.
    """
    
    # A generator expression to flatten the input into a stream of tokens (words/numbers).
    tokens_iterator = (token for line in sys.stdin for token in line.split())

    # Main loop to process all test cases.
    # The loop breaks when the input stream is exhausted.
    while True:
        try:
            # Read the number of words (n) and the number of results to show (k).
            # next() will raise StopIteration at the end of input, which is caught below.
            n = int(next(tokens_iterator))
            k = int(next(tokens_iterator))

            # Read the next n tokens from the input stream.
            words = [next(tokens_iterator) for _ in range(n)]

            # Use collections.Counter to count word frequencies efficiently.
            counts = Counter(words)

            # Convert the counter items to a list and sort it.
            # The sorting criteria are:
            # 1. Frequency in descending order (achieved by negating the count).
            # 2. Word in ascending lexicographical order (the default for strings).
            sorted_items = sorted(counts.items(), key=lambda item: (-item[1], item[0]))

            # Print the first k words from the sorted list.
            for i in range(k):
                print(sorted_items[i][0])
            
            # Print the separator line after each test case.
            print("----------")

        except StopIteration:
            # This exception signals the end of the input stream.
            # We break the loop to terminate the program.
            break

if __name__ == "__main__":
    solve()
