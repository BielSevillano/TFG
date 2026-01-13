
import sys
from collections import Counter

def solve():
    """
    Reads all input, processes each test case for most frequent words,
    and prints the results according to the problem specification.
    """
    try:
        # Read the entire standard input and split it into tokens.
        # This approach is robust for inputs where words and numbers
        # are separated by any whitespace (spaces, newlines, etc.).
        tokens = sys.stdin.read().split()
    except (IOError, IndexError):
        # Gracefully handle empty or problematic input streams.
        return

    # If there are no tokens, there's nothing to process.
    if not tokens:
        return

    # Use an index to iterate through the flat list of tokens.
    idx = 0
    num_tokens = len(tokens)
    
    # Process test cases as long as there are tokens left to form a case.
    while idx < num_tokens:
        try:
            # Each test case begins with two integers, n and k.
            n = int(tokens[idx])
            k = int(tokens[idx + 1])
            idx += 2
        except (ValueError, IndexError):
            # Stop if we can't read n and k, indicating the end of
            # valid input or a malformed test case.
            break

        # Ensure there are enough tokens remaining for the n words.
        if idx + n > num_tokens:
            break
        
        # Extract the n words for the current case.
        words = tokens[idx:idx + n]
        idx += n
        
        # Use collections.Counter for an efficient way to count word frequencies.
        word_counts = Counter(words)
        
        # Sort the items (word, count pairs) based on the specified criteria:
        # 1. Primary key: Frequency in descending order. Achieved by sorting on the
        #    negative of the count.
        # 2. Secondary key (for ties): The word itself, in ascending lexicographical
        #    (alphabetical) order.
        sorted_items = sorted(word_counts.items(), key=lambda item: (-item[1], item[0]))
        
        # Print the first k words from the sorted list.
        # The problem guarantees 1 <= k <= number of unique words, so we don't
        # need to check if the index is out of bounds.
        for i in range(k):
            print(sorted_items[i][0])
            
        # Print the required separator after each test case's output.
        print("----------")

# Execute the main logic of the program.
solve()
