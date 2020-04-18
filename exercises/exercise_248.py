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
    

if __name__ == "__main__":
    print(gcd(34, 17))
    print(gcd(45, 10))
    print(gcd(17, 13))
    #print(gcd(10, 45))


