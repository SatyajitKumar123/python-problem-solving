"""
Problem:
Write a function to check if a number is prime.

Approach:
A prime number is only divisible by 1 and itself. We optimize by checking
divisibility only up to the squre root of n, since any factor larger that √n
would have a corresponding factor smaller than √n.
"""

def is_prime(n: int) -> bool:
    """Return True if n is prime, False otherwise."""
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


if __name__=="__main__":
    test_cases = [2, 3, 4, 17, 29, 100, 1, 0, -5]
    for num in test_cases:
        print(f"is_prime({num}) = {is_prime(num)}")