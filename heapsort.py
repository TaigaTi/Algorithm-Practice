def buildheap(A):
    """
    Builds a max heap from the given list A.

    Parameters:
    A (list): The list to be transformed into a max heap
    """
    for i in range(len(A) // 2, -1, -1):
        heapify(A, len(A), i)

def heapify(A, n, i):
    """
    Heapifies a subtree rooted at index i in the list A.

    Parameters:
    A (list): The list to be heapified
    n (int): The length of the list
    i (int): The index of the subtree to be heapified

    Returns:
    list: The heapified list
    """

    largest = i
    l = 2 * i + 1
    r = 2 * i + 2

    if l < n and A[l] > A[largest]:
        largest = l

    if r < n and A[r] > A[largest]:
        largest = r

    if largest != i:
        A[i], A[largest] = A[largest], A[i]
        heapify(A, n, largest)
        
    return A

def heapsort(A):
    """
    Sorts an array using the Heapsort algorithm.

    Parameters:
    A (list): The list to be sorted

    Returns:
    list: The sorted list
    """
    buildheap(A)
    for i in range(len(A) - 1, 0, -1):
        A[0], A[i] = A[i], A[0]
        heapify(A, i, 0)
        
    return A

A = [5, 2, 31, 17, 8, 24, 1]

print(heapsort(A))