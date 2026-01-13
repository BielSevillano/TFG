
import sys
from collections import Counter
import heapq

# Read all tokens from standard input at once. This approach is generally fast
# and handles various spacings (spaces, newlines) between tokens seamlessly.
try:
    tokens = sys.stdin.read().split()
except IOError:
    tokens = []

# If the input is empty, the tokens list will be empty, and the program will do nothing.
token_idx = 0
while token_idx < len(tokens):
    # Each test case begins with two integers: n (number of words) and k.
    try:
        n = int(tokens[token_idx])
        k = int(tokens[token_idx + 1])
    except (ValueError, IndexError):
        # This handles malformed input or the end of the token list.
        break
    
    token_idx += 2

    # The next 'n' tokens are the words for the current case.
    # We slice the list to get them.
    words = tokens[token_idx : token_idx + n]
    token_idx += n

    # Use collections.Counter to efficiently count the frequency of each word.
    word_counts = Counter(words)

    # To find the top k words, we need to sort by frequency (descending) and
    # then by word (lexicographically ascending) in case of a tie.
    # A standard Python sorting key for this is a tuple: (-frequency, word).
    # The negative sign on the frequency achieves descending order.

    # Instead of a full sort of all unique words (which would be O(U log U), where U
    # is the number of unique words), we can use heapq.nsmallest. This is more
    # efficient (O(U log k)) when k is significantly smaller than U.
    
    # We create a generator to produce the (key, word) tuples for nsmallest.
    # The key is (-count, word), and the item itself is the word. We just need the key.
    items_with_key = ((-count, word) for word, count in word_counts.items())

    # Get the k items with the "smallest" keys.
    top_k_items = heapq.nsmallest(k, items_with_key)

    # The result is a list of tuples, e.g., [(-3, 'cat'), (-2, 'dog')].
    # We iterate through this list and print the word part of each tuple.
    for _, word in top_k_items:
        print(word)

    # As required, print a separator line after each case's output.
    print("----------")

