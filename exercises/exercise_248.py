"""
The first number n for which φ(n)=13! is 6227180929.

Find the 150,000th such number.

φ(n) function documenation:
https://en.wikipedia.org/wiki/Euler%27s_totient_function
"""

def gcd(a: int, b: int) -> 1:
    """
    Find greatest common divisor of two numbers
    requirement a >= b
    """
    if b == 0:
        return a
    return gcd(b, a % b)
    
def is_prime(n: int) -> bool:
    for i in range(2, round(n**(1/2)) + 1):
        if n % i == 0:
            return False
    return True 

def phi(n: int) -> int:
    """Euler's tatient function"""
    if is_prime(n):
        return n - 1
    counter = 0
    for i in range(1, n):
        if gcd(n, i) == 1:
            counter += 1
    return counter

def phi(n: int) -> int:  
  
    result = n   # Initialize result as n 

    # Consider all prime factors 
    # of n and for every prime 
    # factor p, multiply result with (1 - 1 / p)
    p = 2
    while(p*p <= n) : 
        # Check if p is a prime factor. 
        if (n % p == 0) : 
            # If yes, then update n and result 
            while (n % p == 0): 
                n = n // p
            result *= (1.0 - (1.0 / (float) (p))) 
        p += 1
    # If n has a prime factor 
    # greater than sqrt(n) 
    # (There can be at-most one 
    # such prime factor) 
    if (n > 1) : 
        result *= (1.0 - (1.0 / (float)(n))) 
   
    return result


if __name__ == "__main__":
    print(gcd(34, 17))
    print(gcd(45, 10))
    print(gcd(17, 13))
    #print(gcd(10, 45))

    assert phi(223) == 222
    assert phi(211) == 210
    assert phi(232) == 112
    assert phi(316) == 156
    import math
    assert phi(6227180929) == math.factorial(13)

