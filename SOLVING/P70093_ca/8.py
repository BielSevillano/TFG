
def fusio(v1, v2):
    """
    Merges two sorted lists v1 and v2 into a single sorted list,
    without removing duplicate elements.
    v1 and v2 are lists of floats, sorted in non-decreasing order.
    Returns a new sorted list containing all elements from v1 and v2.
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

    # After the main loop, one of the lists might have remaining elements.
    # Append the rest of v1 (if any). The slice will be empty if i is at the end.
    result.extend(v1[i:])

    # Append the rest of v2 (if any). The slice will be empty if j is at the end.
    result.extend(v2[j:])

    return result
