
def merge(v1: list[float], v2: list[float]) -> list[float]:
    """
    Merges two sorted lists of floats v1 and v2 and returns the result.
    Repeated elements are included. The input lists must be sorted.
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
    result.extend(v1[i:])

    # Append the remaining elements from v2, if any
    result.extend(v2[j:])

    return result
