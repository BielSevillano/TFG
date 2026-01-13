
from typing import List

def fusio(v1: List[float], v2: List[float]) -> List[float]:
    """
    Merges two sorted lists of floats v1 and v2 into a new sorted list,
    keeping all elements, including duplicates.
    """
    n1 = len(v1)
    n2 = len(v2)
    
    i = 0
    j = 0
    
    result = []
    
    # Traverse both lists and append the smaller element to the result
    while i < n1 and j < n2:
        if v1[i] <= v2[j]:
            result.append(v1[i])
            i += 1
        else:
            result.append(v2[j])
            j += 1
            
    # At this point, one of the lists is exhausted.
    # Append the remaining elements from the other list.
    # Only one of these slices will be non-empty.
    result.extend(v1[i:])
    result.extend(v2[j:])
    
    return result

