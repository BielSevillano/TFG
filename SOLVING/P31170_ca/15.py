
def main():
    try:
        n = int(input())
        for i in range(1, 11):
            result = n * i
            print(f"{n} x {i} = {result}")
    except (EOFError, ValueError):
        pass

if __name__ == "__main__":
    main()
