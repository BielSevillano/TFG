
def merge(v1, v2):
    """
    Merges two sorted lists v1 and v2 into a single sorted list.
    Repeated elements are included.
    Precondition: v1 and v2 are sorted in non-decreasing order.
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

    # Append the remaining elements of v1, if any
    # Slicing is an efficient way to get the rest of the list
    result.extend(v1[i:])

    # Append the remaining elements of v2, if any
    result.extend(v2[j:])

    return result

