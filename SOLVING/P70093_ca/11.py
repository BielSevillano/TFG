
def fusio(v1: list[float], v2: list[float]) -> list[float]:
    """
    Merges two sorted lists of floats into a single sorted list,
    without removing duplicates.
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

    # Append the remaining elements from v1, if any
    while i < len1:
        result.append(v1[i])
        i += 1

    # Append the remaining elements from v2, if any
    while j < len2:
        result.append(v2[j])
        j += 1

    return result
