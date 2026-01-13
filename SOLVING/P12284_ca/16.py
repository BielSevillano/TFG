
import sys
from collections import Counter

def main():
    """
    Reads multiple test cases of n, k, and n words,
    and for each case, prints the k most frequent words.
    """
    try:
        input_tokens = sys.stdin.read().split()
    except IOError:
        return
    
    if not input_tokens:
        return

    current_token_index = 0
    
    while current_token_index < len(input_tokens):
        try:
            n = int(input_tokens[current_token_index])
            k = int(input_tokens[current_token_index + 1])
            current_token_index += 2
        except (ValueError, IndexError):
            break
            
        words = input_tokens[current_token_index : current_token_index + n]
        current_token_index += n

        word_counts = Counter(words)

        sorted_unique_words = sorted(
            word_counts.keys(), 
            key=lambda word: (-word_counts[word], word)
        )
        
        for i in range(k):
            print(sorted_unique_words[i])
            
        print("----------")

if __name__ == "__main__":
    main()
