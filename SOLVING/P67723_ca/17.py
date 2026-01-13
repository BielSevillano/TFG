
import sys

def mcd(a, b):
    """
    Calcula el màxim comú divisor de a i b usant l'algorisme d'Euclides.
    """
    while b:
        a, b = b, a % b
    return a

for line in sys.stdin:
    try:
        a, b = map(int, line.split())
        result = mcd(a, b)
        print(result)
    except (ValueError, IndexError):
        # Ignora línies buides o mal formades
        pass
