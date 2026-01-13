
def fusio(v1, v2):
    """
    Merges two sorted lists of floats into a single sorted list,
    without removing duplicate elements.
    """
    res = []
    i = 0
    j = 0
    n1 = len(v1)
    n2 = len(v2)

    # Merge the two lists while there are elements in both
    while i < n1 and j < n2:
        if v1[i] <= v2[j]:
            res.append(v1[i])
            i += 1
        else:
            res.append(v2[j])
            j += 1

    # Append the remaining elements from v1, if any
    res.extend(v1[i:])

    # Append the remaining elements from v2, if any
    res.extend(v2[j:])

    return res

