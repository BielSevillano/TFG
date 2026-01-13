
from typing import List

def fusio(v1: List[float], v2: List[float]) -> List[float]:
    """
    Merges two sorted lists v1 and v2 into a new sorted list,
    without removing duplicate elements.
    """
    result = []
    i = 0
    j = 0
    len1 = len(v1)
    len2 = len(v2)

    # Traverse both lists and append the smaller element to the result
    while i < len1 and j < len2:
        if v1[i] <= v2[j]:
            result.append(v1[i])
            i += 1
        else:
            result.append(v2[j])
            j += 1

    # After the loop, one of the lists might have remaining elements.
    # Append the rest of v1 (if any).
    # If v1 is exhausted, v1[i:] will be an empty list.
    result.extend(v1[i:])

    # Append the rest of v2 (if any).
    # If v2 is exhausted, v2[j:] will be an empty list.
    result.extend(v2[j:])

    return result
