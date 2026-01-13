
def fusio(v1, v2):
    """
    Merges two sorted lists v1 and v2 and returns the result.
    Repeated elements are not removed.
    Precondition: v1 and v2 are sorted in ascending order.
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

    # Append the remaining elements from the list that is not exhausted.
    # One of these slices will be empty.
    result.extend(v1[i:])
    result.extend(v2[j:])

    return result
