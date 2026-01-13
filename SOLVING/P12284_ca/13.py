
import sys
from collections import Counter

def solve():
    """
    Main function to read test cases from stdin and solve the problem.
    """
    # Read the first line of a potential test case
    line = sys.stdin.readline()
    
    # Loop as long as there is input
    while line:
        # Strip whitespace. If the line was just a newline, it becomes empty.
        line = line.strip()
        
        # If the line is empty (e.g., blank lines between test cases),
        # try to read the next one and continue the loop.
        if not line:
            line = sys.stdin.readline()
            continue

        # Parse n and k from the line
        try:
            n, k = map(int, line.split())
        except (ValueError, IndexError):
            # Exit if the line is not in the expected "n k" format
            break

        # Read the n words for the current test case.
        # .strip() is important to remove the trailing newline.
        words = [sys.stdin.readline().strip() for _ in range(n)]

        # Count frequencies of each word efficiently
        counts = Counter(words)
        
        # Sort the items (word, count pairs) from the counter.
        # The sorting key is a tuple: (-count, word).
        # This achieves sorting by count in descending order (due to the negation)
        # and then by word in ascending lexicographical order for ties.
        sorted_items = sorted(counts.items(), key=lambda item: (-item[1], item[0]))
        
        # Print the first k words from the sorted list
        for i in range(k):
            print(sorted_items[i][0])
            
        # Print the required separator
        print("----------")
        
        # Read the line that starts the next test case for the next iteration
        line = sys.stdin.readline()

# Run the solution
solve()
