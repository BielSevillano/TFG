
from typing import List

def fusio(v1: List[float], v2: List[float]) -> List[float]:
    """
    Merges two sorted lists v1 and v2 into a new sorted list,
    without removing duplicate elements.
    """
    n1 = len(v1)
    n2 = len(v2)
    i = 0
    j = 0
    result: List[float] = []

    # Traverse both lists while there are elements in both
    while i < n1 and j < n2:
        if v1[i] <= v2[j]:
            result.append(v1[i])
            i += 1
        else:
            result.append(v2[j])
            j += 1

    # Append the remaining elements from v1, if any
    result.extend(v1[i:])
    
    # Append the remaining elements from v2, if any
    result.extend(v2[j:])
    
    return result

