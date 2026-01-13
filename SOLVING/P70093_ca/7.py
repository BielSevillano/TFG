
from typing import List

def fusio(v1: List[float], v2: List[float]) -> List[float]:
    """
    Merges two sorted lists, v1 and v2, and returns the result.
    Repeated elements are not removed.
    Precondition: v1 and v2 are sorted in non-decreasing order.
    """
    i = 0
    j = 0
    len_v1 = len(v1)
    len_v2 = len(v2)
    
    result = []
    
    # Merge the two lists while there are elements in both
    while i < len_v1 and j < len_v2:
        if v1[i] <= v2[j]:
            result.append(v1[i])
            i += 1
        else:
            result.append(v2[j])
            j += 1
            
    # Append the remaining elements from v1, if any
    # This is more efficient than a second while loop
    # as it's a single block memory operation.
    # The slice will be empty for the list that was fully traversed.
    result.extend(v1[i:])
    
    # Append the remaining elements from v2, if any
    result.extend(v2[j:])
        
    return result
