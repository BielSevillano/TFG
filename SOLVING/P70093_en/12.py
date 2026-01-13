
from typing import List

def merge(v1: List[float], v2: List[float]) -> List[float]:
    """
    Merges two sorted lists of floats into a single sorted list.
    """
    n1, n2 = len(v1), len(v2)
    result = [0.0] * (n1 + n2)
    i, j, k = 0, 0, 0

    # Traverse both lists while there are elements in both
    while i < n1 and j < n2:
        if v1[i] <= v2[j]:
            result[k] = v1[i]
            i += 1
        else:
            result[k] = v2[j]
            j += 1
        k += 1

    # Copy any remaining elements from v1
    while i < n1:
        result[k] = v1[i]
        i += 1
        k += 1

    # Copy any remaining elements from v2
    while j < n2:
        result[k] = v2[j]
        j += 1
        k += 1

    return result
