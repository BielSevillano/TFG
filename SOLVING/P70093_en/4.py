
def merge(v1: list[float], v2: list[float]) -> list[float]:
    """
    Merges two sorted lists of floats into a single sorted list,
    including repeated elements.
    """
    result = []
    i, j = 0, 0
    n1, n2 = len(v1), len(v2)

    # Traverse both lists and append the smaller element to the result
    while i < n1 and j < n2:
        if v1[i] <= v2[j]:
            result.append(v1[i])
            i += 1
        else:
            result.append(v2[j])
            j += 1

    # Append the remaining elements from the list that is not exhausted
    # One of these extend calls will be with an empty slice
    result.extend(v1[i:])
    result.extend(v2[j:])

    return result
