
from typing import List

def fusio(v1: List[float], v2: List[float]) -> List[float]:
    """
    Merges two sorted lists v1 and v2 into a new sorted list,
    without removing duplicates.
    """
    result = []
    i = 0
    j = 0
    len1 = len(v1)
    len2 = len(v2)

    # Iterate while both lists have elements
    while i < len1 and j < len2:
        if v1[i] <= v2[j]:
            result.append(v1[i])
            i += 1
        else:
            result.append(v2[j])
            j += 1

    # Append any remaining elements from v1
    # This loop will run only if v2 is exhausted first
    while i < len1:
        result.append(v1[i])
        i += 1

    # Append any remaining elements from v2
    # This loop will run only if v1 is exhausted first
    while j < len2:
        result.append(v2[j])
        j += 1

    return result

