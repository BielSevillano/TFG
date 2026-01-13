
def main():
    try:
        n = int(input())
        if 1 <= n <= 9:
            for i in range(1, 11):
                result = n * i
                print(f"{n} x {i} = {result}")
    except (EOFError, ValueError):
        # The problem statement implies a single valid input,
        # but robust code handles potential empty or invalid input.
        # Jutge.org environment will provide valid input as described.
        pass

if __name__ == "__main__":
    main()
