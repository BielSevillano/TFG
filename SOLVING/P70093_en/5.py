
from typing import List

def merge(v1: List[float], v2: List[float]) -> List[float]:
    """
    Merges two sorted lists of floats into a single sorted list.
    """
    result: List[float] = []
    i = 0
    j = 0
    len1 = len(v1)
    len2 = len(v2)

    # Merge elements from both lists in sorted order
    while i < len1 and j < len2:
        if v1[i] <= v2[j]:
            result.append(v1[i])
            i += 1
        else:
            result.append(v2[j])
            j += 1

    # Append any remaining elements from v1
    # (only one of these extend calls will do anything)
    result.extend(v1[i:])

    # Append any remaining elements from v2
    result.extend(v2[j:])

    return result
