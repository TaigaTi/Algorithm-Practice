def merge(B, C):
    """
    Merges two sorted lists B and C into a single sorted list A.
    
    Parameters:
    B (list): The first sorted list
    C (list): The second sorted list
    
    Returns:
    list: A single sorted list containing all elements from B and C
    """
    A = [0] * (len(B) + len(C))

    i = 0
    j = 0
    k = 0
    
    while (i < len(B) and j < len(C)):
        if (B[i] <= C[j]):
            A[k] = B[i]
            i += 1
        else:
            A[k] = C[j]
            j+=1
        
        k += 1
        
    if (i == len(B)):
        while j < len(C):
            A[k] = C[j]
            j += 1
            k += 1
            
    else:
        while i < len(B):
            A[k] = B[i]
            i += 1
            k += 1
            
    return A

def mergesort(A):
    """
    Sorts an array using the mergesort algorithm.

    Parameters:
    A (list): The list to be sorted

    Returns:
    list: The sorted list
    """
    if (len(A) > 1): 
        mid = len(A) // 2
    
        B = A[:mid]
        C = A[mid:]
        
        mergesort(B)
        mergesort(C)
        A[:] = merge(B, C)
        
        return A

B = [3, 5, 4, 6, 8, 1, 2, 92, 3, 4]

print(mergesort(B))