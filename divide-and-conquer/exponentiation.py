def exponentiation(a, n):
    """
    Returns the value of an integer a raised to the power of n using the
    divide and conquer approach.

    Parameters:
    a (int): The base number
    n (int): The exponent

    Returns:
    int: The value of a raised to the power of n
    """
    if n == 0:
        return 1
    
    if n % 2 == 0:
        half_pow = exponentiation(a, n // 2)
        return half_pow * half_pow
    else:
        half_pow = exponentiation(a, n // 2)
        return a * half_pow * half_pow

print(exponentiation(2, 3))
