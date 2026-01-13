
import sys
from collections import Counter

def solve():
    """
    Reads all input, processes test cases, and prints the k most frequent words.
    """
    try:
        # Read all whitespace-separated tokens from stdin at once.
        # This approach is simple and robust for the given problem format.
        all_tokens = sys.stdin.read().split()
    except (IOError, IndexError):
        # Handle potential empty input or read errors gracefully.
        all_tokens = []

    # An index to iterate through the tokens.
    idx = 0
    while idx < len(all_tokens):
        try:
            # Parse n and k for the current test case.
            n = int(all_tokens[idx])
            k = int(all_tokens[idx + 1])
            idx += 2
            
            # Slice the list to get the n words for this case.
            words = all_tokens[idx : idx + n]
            idx += n
        except (ValueError, IndexError):
            # If input is malformed (e.g., not enough tokens), stop processing.
            break

        # Use collections.Counter for efficient frequency counting.
        word_frequencies = Counter(words)
        
        # Sort the unique words based on the specified criteria:
        # 1. Frequency in descending order (achieved by using -frequency).
        # 2. Lexicographical order for ties (word itself is the secondary key).
        sorted_word_list = sorted(word_frequencies.items(), key=lambda item: (-item[1], item[0]))
        
        # As per the problem statement, k is at most the number of unique words,
        # so we can safely iterate up to k.
        for i in range(k):
            print(sorted_word_list[i][0])
            
        # Print the separator after each test case.
        print("----------")

solve()
