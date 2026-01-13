
def merge(v1: list[float], v2: list[float]) -> list[float]:
    """
    Merges two sorted lists v1 and v2 and returns the result.
    Repeated elements are included.
    """
    result = []
    i = 0
    j = 0
    len_v1 = len(v1)
    len_v2 = len(v2)

    # Traverse both lists until one is exhausted
    while i < len_v1 and j < len_v2:
        if v1[i] <= v2[j]:
            result.append(v1[i])
            i += 1
        else:
            result.append(v2[j])
            j += 1

    # Append the remaining elements from v1, if any
    while i < len_v1:
        result.append(v1[i])
        i += 1

    # Append the remaining elements from v2, if any
    while j < len_v2:
        result.append(v2[j])
        j += 1

    return result

