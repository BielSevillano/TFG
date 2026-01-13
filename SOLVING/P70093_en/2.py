
def merge(v1, v2):
    """
    Merges two sorted lists v1 and v2 and returns the result,
    repeated elements included.
    Precondition: v1 and v2 are sorted in nondecreasing order.
    """
    result = []
    i = 0
    j = 0
    len1 = len(v1)
    len2 = len(v2)

    # Traverse both lists and append the smaller element
    while i < len1 and j < len2:
        if v1[i] <= v2[j]:
            result.append(v1[i])
            i += 1
        else:
            result.append(v2[j])
            j += 1

    # Append the remaining elements of the list that is not exhausted.
    # At most one of the following slices will contain elements.
    result.extend(v1[i:])
    result.extend(v2[j:])

    return result

