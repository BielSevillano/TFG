
def fusio(v1: list[float], v2: list[float]) -> list[float]:
    """
    Merges two sorted lists v1 and v2 into a single sorted list,
    without removing duplicates.
    """
    resultat = []
    i = 0  # Pointer for v1
    j = 0  # Pointer for v2
    n1 = len(v1)
    n2 = len(v2)

    # Traverse both lists and append the smaller element
    while i < n1 and j < n2:
        if v1[i] <= v2[j]:
            resultat.append(v1[i])
            i += 1
        else:
            resultat.append(v2[j])
            j += 1

    # Append the remaining elements from the list that is not exhausted.
    # At this point, one of the lists is fully traversed, so one of the
    # following slices will be empty.
    resultat.extend(v1[i:])
    resultat.extend(v2[j:])

    return resultat
