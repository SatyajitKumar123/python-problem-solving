# Recursive Factorial Calculator
""" 
Real-World Use: Mathematical calculations, permutations, combinatorics.
"""


def factorial(n):
    """ 
    Calculates n! recursively.
    Example: 5! = 5 * 4 * 3 * 2 * 1
    """
    if n < 0:
        raise ValueError("Negative numbers not allowed")
    if n == 0 or n == 1:
        return 1
    return n * factorial(n -1)


if __name__=="__main__":
    factorial()