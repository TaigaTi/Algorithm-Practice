def LomutoPartition(A, left, right):
    """
    Implements the Lomuto Partition Scheme for Quicksort,

    Parameters:
    A (list): The list to be partitioned
    left (int): The left index of the list
    right (int): The right index of the list

    Returns:
    int: The index of the pivot element in its final sorted position
    """
    partition = A[right]
    i = left - 1
    
    for j in range(left, right):
        if A[j] < partition:
            i += 1
            A[i], A[j] = A[j], A[i]
    
    A[i + 1], A[right] = A[right], A[i + 1]
    
    return i + 1

def quicksort(A, left, right):
    """
    Recursively sorts an array using the quicksort algorithm with the Lomuto partition
    scheme.

    Parameters:
    A (list): The list to be sorted
    left (int): The left index of the list
    right (int): The right index of the list

    Returns:
    list: The sorted list
    """
    if left < right:
        pivot = LomutoPartition(A, left, right)
        quicksort(A, left, pivot - 1)
        quicksort(A, pivot + 1, right)
        
    return A

A = [5, 2, 31, 17, 8, 24, 1]

print(quicksort(A, 0, len(A) - 1))