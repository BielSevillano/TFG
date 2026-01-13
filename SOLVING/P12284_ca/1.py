
import sys
from collections import Counter

def solve():
    """
    Reads all test cases from stdin and processes them.
    """
    # Read the first line to start the loop
    line = sys.stdin.readline()
    
    while line:
        # Strip potential whitespace and check if the line is empty
        line = line.strip()
        if not line:
            # If line is empty (e.g., blank line between cases), read next and continue
            line = sys.stdin.readline()
            continue

        try:
            n, k = map(int, line.split())
        except (ValueError, IndexError):
            # This should not happen with valid input but handles malformed lines
            break
            
        # Read the n words for the current case
        words = [sys.stdin.readline().strip() for _ in range(n)]
        
        # Count the frequencies of the words using collections.Counter
        word_counts = Counter(words)
        
        # Get the items (word, count) and sort them.
        # The key for sorting is a tuple: (-count, word).
        # The negative sign on count sorts frequencies in descending order.
        # The word itself sorts lexicographically (ascending) for ties.
        sorted_items = sorted(word_counts.items(), key=lambda item: (-item[1], item[0]))
        
        # Print the top k words from the sorted list
        for i in range(k):
            print(sorted_items[i][0])
            
        # Print the separator
        print('----------')
        
        # Read the line that starts the next test case
        line = sys.stdin.readline()

solve()
