
def merge(v1: list[float], v2: list[float]) -> list[float]:
    """
    Merges two sorted lists of floats into a single sorted list.
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

    # At this point, one of the lists has been fully traversed.
    # The remaining elements in the other list are appended.
    # Note that one of v1[i:] or v2[j:] will be an empty list.
    result.extend(v1[i:])
    result.extend(v2[j:])

    return result
