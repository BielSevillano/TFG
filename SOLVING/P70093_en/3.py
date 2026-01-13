
def merge(v1, v2):
    """
    Merges two sorted lists of floats into a single sorted list.
    """
    i = 0
    j = 0
    result = []
    len1 = len(v1)
    len2 = len(v2)

    while i < len1 and j < len2:
        if v1[i] <= v2[j]:
            result.append(v1[i])
            i += 1
        else:
            result.append(v2[j])
            j += 1

    # Append the remaining elements from the list that is not exhausted.
    # One of these extend calls will be on an empty slice.
    result.extend(v1[i:])
    result.extend(v2[j:])

    return result
