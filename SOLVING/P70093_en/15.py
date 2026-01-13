
def merge(v1: list[float], v2: list[float]) -> list[float]:
    """
    Merges two sorted lists of floats v1 and v2 into a new sorted list,
    including repeated elements.
    """
    result: list[float] = []
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

    # After the main loop, one of the lists might have remaining elements.
    # Append the rest of v1 to the result. If v1 is exhausted, v1[i:] will be empty.
    result.extend(v1[i:])
    
    # Append the rest of v2 to the result. If v2 is exhausted, v2[j:] will be empty.
    result.extend(v2[j:])
    
    return result
