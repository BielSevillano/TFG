
from typing import List

def merge(v1: List[float], v2: List[float]) -> List[float]:
    """
    Merges two sorted lists v1 and v2 into a single sorted list,
    including repeated elements.
    """
    result = []
    i, j = 0, 0
    len1, len2 = len(v1), len(v2)

    while i < len1 and j < len2:
        if v1[i] <= v2[j]:
            result.append(v1[i])
            i += 1
        else:
            result.append(v2[j])
            j += 1

    # Append remaining elements from the list that is not exhausted.
    # One of these slices will be empty.
    result.extend(v1[i:])
    result.extend(v2[j:])

    return result

