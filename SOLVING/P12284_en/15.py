
import sys
from collections import Counter

def main():
    """
    Reads all input, processes test cases for most frequent words, and prints the results.
    """
    try:
        tokens = sys.stdin.read().split()
    except IOError:
        tokens = []

    if not tokens:
        return

    token_idx = 0
    while token_idx < len(tokens):
        try:
            n = int(tokens[token_idx])
            k = int(tokens[token_idx + 1])
            token_idx += 2
        except (ValueError, IndexError):
            # This handles incomplete input at the end of the file.
            break

        # It's assumed that if n and k are present, n words follow.
        words_for_case = tokens[token_idx : token_idx + n]
        token_idx += n

        # Use collections.Counter for efficient frequency counting.
        word_counts = Counter(words_for_case)

        # Sort the items based on the specified criteria:
        # 1. Frequency in descending order (-item[1]).
        # 2. Word in lexicographical (alphabetical) ascending order (item[0]).
        sorted_items = sorted(word_counts.items(), key=lambda item: (-item[1], item[0]))

        # Print the top k words.
        for i in range(k):
            print(sorted_items[i][0])

        # Print the separator line.
        print("----------")

if __name__ == "__main__":
    main()
