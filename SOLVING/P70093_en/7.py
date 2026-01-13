
def merge(v1: list[float], v2: list[float]) -> list[float]:
    """
    Merges two sorted lists of floats into a single sorted list.
    Repeated elements are included.
    Precondition: v1 and v2 are sorted in non-decreasing order.
    """
    result = []
    i = 0
    j = 0
    len1 = len(v1)
    len2 = len(v2)

    # Traverse both lists while there are elements in both
    while i < len1 and j < len2:
        if v1[i] <= v2[j]:
            result.append(v1[i])
            i += 1
        else:
            result.append(v2[j])
            j += 1

    # At this point, one of the lists is exhausted.
    # Append the remaining elements from the other list.
    # One of these slices will be empty.
    result.extend(v1[i:])
    result.extend(v2[j:])

    return result
