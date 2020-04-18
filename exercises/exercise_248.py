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
    raise NotImplemented


if __name__ == "__main__":
    print(gcd(34, 17))
    print(gcd(45, 10))
    print(gcd(17, 13))
    #print(gcd(10, 45))

    assert phi(223) == 222
    assert phi(211) == 210


