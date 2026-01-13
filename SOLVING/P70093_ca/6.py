
def fusio(v1, v2):
    """
    Merges two sorted lists v1 and v2 into a new sorted list,
    without removing duplicate elements.
    """
    result = []
    i = 0
    j = 0
    len1 = len(v1)
    len2 = len(v2)

    while i < len1 and j < len2:
        if v1[i] <= v2[j]:
            result.append(v1[i])
            i += 1
        else:
            result.append(v2[j])
            j += 1

    # At this point, one of the lists has been fully traversed.
    # Append the remaining elements from the other list.
    # One of these slices will be empty.
    result.extend(v1[i:])
    result.extend(v2[j:])

    return result
