
from typing import List

def merge(v1: List[float], v2: List[float]) -> List[float]:
    """
    Merges two sorted lists v1 and v2 into a single sorted list,
    including repeated elements.
    """
    n1 = len(v1)
    n2 = len(v2)
    result = []
    i = 0
    j = 0

    # Traverse both lists and append the smaller element to the result
    while i < n1 and j < n2:
        if v1[i] <= v2[j]:
            result.append(v1[i])
            i += 1
        else:
            result.append(v2[j])
            j += 1

    # Append the remaining elements of v1, if any
    while i < n1:
        result.append(v1[i])
        i += 1

    # Append the remaining elements of v2, if any
    while j < n2:
        result.append(v2[j])
        j += 1

    return result

