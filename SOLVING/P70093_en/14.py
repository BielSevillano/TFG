
def merge(v1, v2):
    """
    Merges two sorted lists v1 and v2 into a single sorted list.
    v1 and v2 are assumed to be sorted in non-decreasing order.
    The result includes repeated elements.
    """
    result = []
    i = 0
    j = 0
    len_v1 = len(v1)
    len_v2 = len(v2)

    # Traverse both lists and append the smaller element to the result
    while i < len_v1 and j < len_v2:
        if v1[i] <= v2[j]:
            result.append(v1[i])
            i += 1
        else:
            result.append(v2[j])
            j += 1

    # After the main loop, one of the lists might have remaining elements.
    # Append the rest of v1, if any.
    result.extend(v1[i:])
    
    # Append the rest of v2, if any.
    result.extend(v2[j:])

    return result
