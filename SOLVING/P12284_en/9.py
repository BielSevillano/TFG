
import sys
from collections import Counter

def solve():
    """
    Reads all test cases from stdin and processes them.
    This function encapsulates the logic to be executed.
    """
    while True:
        # Read the line that should contain n and k
        line = sys.stdin.readline()
        
        # An empty line indicates the end of the input (EOF)
        if not line:
            break

        try:
            # Parse n and k. Skip the line if it's malformed or empty.
            n, k = map(int, line.split())
        except (ValueError, IndexError):
            continue

        # Handle the edge case where n is 0.
        # The loop for reading words won't run, so we just print the separator.
        if n == 0:
            print("----------")
            continue

        # Use a generator expression within the Counter constructor.
        # This is a memory-efficient way to read n words and count their
        # frequencies without storing them all in a list first.
        word_generator = (sys.stdin.readline().strip() for _ in range(n))
        word_counts = Counter(word_generator)

        # Convert the Counter's items to a list and sort it.
        # The sorting key is a tuple: `(-frequency, word)`.
        # - The negative frequency `(-item[1])` ensures descending order for frequency.
        # - The word `(item[0])` ensures ascending lexicographical order for ties.
        sorted_items = sorted(word_counts.items(), key=lambda item: (-item[1], item[0]))

        # The problem guarantees that k is at least 1 and no more than the
        # number of unique words. So, we can safely print the first k items.
        for i in range(k):
            print(sorted_items[i][0])

        # Print the required separator at the end of each test case.
        print("----------")

# Execute the main logic
solve()
