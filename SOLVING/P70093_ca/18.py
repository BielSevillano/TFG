
def fusio(v1, v2):
    """
    Merges two sorted lists v1 and v2 into a single sorted list.
    """
    result = []
    i = 0  # Pointer for v1
    j = 0  # Pointer for v2
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

    # Append the remaining elements of v1, if any
    # This is equivalent to result.extend(v1[i:])
    while i < len1:
        result.append(v1[i])
        i += 1

    # Append the remaining elements of v2, if any
    # This is equivalent to result.extend(v2[j:])
    while j < len2:
        result.append(v2[j])
        j += 1

    return result
