
from typing import List

def fusio(v1: List[float], v2: List[float]) -> List[float]:
    """
    Merges two sorted lists of floats, v1 and v2, and returns the result,
    without removing duplicate elements.
    Precondition: v1 and v2 are sorted in non-decreasing order.
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

    # After the main loop, one of the lists might still have elements.
    # Append the remaining elements from the non-exhausted list.
    # Only one of these extend calls will actually add elements, as the
    # other list's slice will be empty.
    result.extend(v1[i:])
    result.extend(v2[j:])

    return result
