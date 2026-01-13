
from typing import List

def fusio(v1: list[float], v2: list[float]) -> list[float]:
    """
    Merges two sorted lists, v1 and v2, and returns the result,
    without removing duplicate elements.
    """
    resultat = []
    i = 0
    j = 0
    n1 = len(v1)
    n2 = len(v2)

    # Traverse both lists and append the smaller element to the result
    while i < n1 and j < n2:
        if v1[i] <= v2[j]:
            resultat.append(v1[i])
            i += 1
        else:
            resultat.append(v2[j])
            j += 1

    # After the loop, one of the lists might have remaining elements.
    # Append the rest of the non-exhausted list.
    # One of the following slices will be empty.
    resultat.extend(v1[i:])
    resultat.extend(v2[j:])

    return resultat

