
def main():
    """
    Reads a number n and prints its multiplication table.
    """
    try:
        n = int(input())
        
        # The problem statement guarantees n is between 1 and 9,
        # but a loop from 1 to 10 is standard for multiplication tables.
        for i in range(1, 11):
            result = n * i
            print(f"{n} x {i} = {result}")

    except (EOFError, ValueError):
        # Handle cases where input is not a valid integer or no input is provided.
        # This part is for robustness, as the problem statement guarantees valid input.
        pass

if __name__ == "__main__":
    main()
