
import sys
from collections import Counter

def main():
    """
    Main function to solve the "Paraules més freqüents" problem.
    It reads multiple test cases from standard input, finds the k most frequent words
    for each case, and prints them according to the specified sorting order.
    """
    try:
        # Read the entire standard input and split it into a list of tokens.
        # This is an efficient way to handle I/O in competitive programming.
        tokens = sys.stdin.read().split()
    except IOError:
        # In case of an I/O error, treat tokens as an empty list.
        tokens = []

    if not tokens:
        return

    # An index to keep track of the current position in the list of tokens.
    token_idx = 0
    
    # Loop through the tokens to process each test case.
    while token_idx < len(tokens):
        try:
            # Each case starts with n (number of words) and k (number to output).
            n = int(tokens[token_idx])
            k = int(tokens[token_idx + 1])
            token_idx += 2
        except (ValueError, IndexError):
            # Stop if we can't parse n and k, indicating the end of valid input.
            break

        # Extract the n words for the current test case.
        words_for_case = tokens[token_idx : token_idx + n]
        
        # Safety check for malformed input where n is larger than remaining tokens.
        if len(words_for_case) < n:
            break
            
        # Move the index past the words just processed.
        token_idx += n

        # Use collections.Counter for efficient frequency counting.
        word_counts = Counter(words_for_case)

        # Sort the items (word, count) based on the specified criteria:
        # 1. Frequency in descending order (-item[1]).
        # 2. Word in lexicographical (alphabetical) ascending order (item[0]) for ties.
        sorted_items = sorted(word_counts.items(), key=lambda item: (-item[1], item[0]))

        # Print the top k words.
        for i in range(k):
            print(sorted_items[i][0])

        # Print the separator line after each test case.
        print("----------")

if __name__ == "__main__":
    main()
