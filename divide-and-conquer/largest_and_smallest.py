def largest_and_smallest(A):
    """
    Returns the largest and smallest number in an array using the divide and conquer approach.
    
    Recurrence - T(n) = 2T(n/2) + 1
    """
    if len(A) > 2:
        mid = len(A) // 2
        res1 = largest_and_smallest(A[:mid])
        res2 = largest_and_smallest(A[mid:])
        return max(res1[0], res2[0]), min(res1[1], res2[1])
    else:
        return max(A), min(A)
    
print(largest_and_smallest([30, 6, 7, 56, 6, 8, 23, 10]))