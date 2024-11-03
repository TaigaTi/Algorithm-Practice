def findLargest(A):
    """
    Returns the largest number in an array using the divide and conquer approach
    
    Recurrence - T(n) = 2T(n/2) + 1
    """
    if len(A) > 2:
        mid = len(A) // 2
        num1 = findLargest(A[:mid])
        num2 = findLargest(A[mid:])
        return max(num1, num2)
    else:
        return max(A)
        
print(findLargest([3, 6, 7, 5, 6, 8, 23, 10]))