
import sys

def solve():
    """
    Reads a sequence of characters ending with a period and counts the number of 'a's.
    """
    
    # Read the entire standard input at once.
    # This is generally more efficient for competitive programming problems
    # than reading character by character due to fewer system I/O calls.
    full_input = sys.stdin.read()
    
    # The problem specifies that the sequence to be processed ends at the
    # first period ('.'). We use split('.', 1) to divide the input string
    # into at most two parts at the first period. We are interested in the
    # part before the period, which is the first element ([0]) of the resulting list.
    try:
        sequence_to_process = full_input.split('.', 1)[0]
    except IndexError:
        # This case would only happen with an empty input,
        # which is unlikely given the problem statement.
        # An empty string is a safe fallback.
        sequence_to_process = ""

    # The string method count() is a highly optimized way to count
    # the number of non-overlapping occurrences of a substring.
    # We use it to count the number of 'a' characters.
    a_count = sequence_to_process.count('a')
    
    # Print the final count to standard output, followed by a newline.
    print(a_count)

solve()
