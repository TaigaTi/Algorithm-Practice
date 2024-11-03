def HoarePartition(A, l, r):
    """
    Implements the Hoare Partition Scheme for Quicksort.

    Parameters:
    A (list): The list to be partitioned
    l (int): The left index of the list
    r (int): The right index of the list

    Returns:
    int: The index of the pivot element in its final sorted position
    """
    p = A[l]
    i = l + 1
    j = r 
    
    while True:
        while (A[i] < p):
            i += 1
        while (A[j] > p):
            j -= 1
        
        if i >= j:
            break
            
        A[i], A[j] = A[j], A[i]
        
        print(A)
        
    A[l], A[j] = A[j], A[l]
    
    return j

A = [5, 2, 31, 17, 8, 24, 1]

def quicksort(A, l, r):
    """
    Recursively sorts an array using the quicksort algorithm with the Hoare partition
    scheme.

    Parameters:
    A (list): The list to be sorted
    l (int): The left index of the list
    r (int): The right index of the list

    Returns:
    list: The sorted list
    """
    
    if (l < r):
        s = HoarePartition(A, l, r)
        quicksort(A, l, s - 1)
        quicksort(A, s + 1, r)
        
    return A
        
print(quicksort(A, 0, len(A) - 1))