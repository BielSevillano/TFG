
from typing import List

def merge(v1: List[float], v2: List[float]) -> List[float]:
    """
    Merges the sorted lists v1 and v2 and returns the result,
    with repeated elements included.
    v1 and v2 are assumed to be sorted in non-decreasing order.
    """
    result = []
    i = 0
    j = 0
    n1 = len(v1)
    n2 = len(v2)

    # Traverse both lists and append the smaller element to the result
    while i < n1 and j < n2:
        if v1[i] <= v2[j]:
            result.append(v1[i])
            i += 1
        else:
            result.append(v2[j])
            j += 1

    # Append the remaining elements from the list that was not fully traversed.
    # One of the following slices will be empty.
    result.extend(v1[i:])
    result.extend(v2[j:])

    return result
