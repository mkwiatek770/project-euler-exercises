"""
The first number n for which φ(n)=13! is 6227180929.

Find the 150,000th such number.

φ(n) function documenation:
https://en.wikipedia.org/wiki/Euler%27s_totient_function
"""

def gcd(a: int, b: int):
    if a > b:
        bigger, smaller = a, b
    else:
        bigger, smaller = a, b
    while True:
        reminder = bigger % smaller
        if reminder == 0:
            return smaller
        bigger = smaller
        smaller = reminder

if __name__ == "__main__":
    print(gcd(34, 17))
    print(gcd(45, 10))
    print(gcd(10, 45))


