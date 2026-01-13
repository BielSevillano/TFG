
def main():
    """
    Reads a number n and prints its multiplication table.
    """
    try:
        n = int(input())
        if 1 <= n <= 9:
            for i in range(1, 11):
                result = n * i
                print(f"{n} x {i} = {result}")
    except (EOFError, ValueError):
        # The program will end if there is no more input or the input is invalid.
        pass

if __name__ == "__main__":
    main()
