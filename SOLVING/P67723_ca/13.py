
import sys

def mcd(a, b):
    """
    Calcula el màxim comú divisor de a i b mitjançant l'algorisme d'Euclides.
    """
    while b:
        a, b = b, a % b
    return a

def main():
    """
    Llegeix parells de nombres de l'entrada estàndard i n'escriu el mcd.
    """
    for line in sys.stdin:
        try:
            # Separem la línia en dos nombres
            a, b = map(int, line.split())
            # Calculem i escrivim el resultat
            print(mcd(a, b))
        except (ValueError, IndexError):
            # Ignorem línies buides o amb format incorrecte
            pass

if __name__ == "__main__":
    main()
