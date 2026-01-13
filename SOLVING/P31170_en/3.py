
def main():
    """
    Reads a number n and prints its multiplication table.
    """
    try:
        n = int(input())
        for i in range(1, 11):
            result = n * i
            print(f"{n} * {i} = {result}")
    except (EOFError, ValueError):
        # The program will end if input stream is closed or input is not a valid number.
        pass

if __name__ == "__main__":
    main()
