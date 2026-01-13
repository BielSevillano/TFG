
from typing import List

def merge(v1: List[float], v2: List[float]) -> List[float]:
    """
    Merges two sorted lists of floats into a single sorted list.
    Repeated elements are included.
    """
    len_v1 = len(v1)
    len_v2 = len(v2)
    
    i = 0
    j = 0
    
    result = []
    
    while i < len_v1 and j < len_v2:
        if v1[i] <= v2[j]:
            result.append(v1[i])
            i += 1
        else:
            result.append(v2[j])
            j += 1
            
    # Append the remaining elements from v1, if any
    result.extend(v1[i:])
    
    # Append the remaining elements from v2, if any
    result.extend(v2[j:])
        
    return result
