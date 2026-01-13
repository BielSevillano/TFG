
import sys

def solve():
    """
    Reads a sequence of characters until a period is found,
    counts the number of 'a's, and prints the count.
    """
    full_input = sys.stdin.read()
    
    # The problem guarantees the input ends with a period.
    # We can split the string by the first period and take the part before it.
    # The split method is a clean way to handle this.
    # split('.', 1) ensures we only split at the very first occurrence.
    try:
        sequence_before_dot = full_input.split('.', 1)[0]
    except IndexError:
        # This case would only happen for an empty input, which is unlikely
        # given the problem statement, but it's good practice to handle.
        sequence_before_dot = ""

    # The string's count() method is highly efficient for this task.
    count = sequence_before_dot.count('a')
    
    print(count)

solve()
