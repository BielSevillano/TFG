
def fusio(v1: list[float], v2: list[float]) -> list[float]:
    """
    Merges two sorted lists v1 and v2 into a single sorted list.
    """
    result = []
    i = 0
    j = 0
    n1 = len(v1)
    n2 = len(v2)

    while i < n1 and j < n2:
        if v1[i] <= v2[j]:
            result.append(v1[i])
            i += 1
        else:
            result.append(v2[j])
            j += 1

    # Append remaining elements from v1, if any
    result.extend(v1[i:])

    # Append remaining elements from v2, if any
    result.extend(v2[j:])

    return result
