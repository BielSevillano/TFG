
def fusio(v1, v2):
    """
    Merges two sorted lists v1 and v2 into a single sorted list,
    keeping duplicate elements.
    """
    result = []
    i = 0
    j = 0
    n1 = len(v1)
    n2 = len(v2)

    # Iterate while there are elements in both lists
    while i < n1 and j < n2:
        if v1[i] <= v2[j]:
            result.append(v1[i])
            i += 1
        else:
            result.append(v2[j])
            j += 1

    # Append any remaining elements from v1
    # This loop will not run if v1 is exhausted
    while i < n1:
        result.append(v1[i])
        i += 1

    # Append any remaining elements from v2
    # This loop will not run if v2 is exhausted
    while j < n2:
        result.append(v2[j])
        j += 1
        
    return result

