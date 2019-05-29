# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
# a2 + b2 = c2

# For example, 32 + 42 = 9 + 16 = 25 = 52.

# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.


def is_triangle(a, b, c):
    return a + b > c and a + c > b and b + c > a

def is_right_triangle(a, b, c):
    return a**2 + b**2 == c**2

def is_special(a, b, c):
    return a + b + c == 1000

def is_equal(a, b):
    return 500000 == 1000*(a + b) - a*b

def special_pythagorean_triplet():
    for a in range(1, 500):
        for b in range(1, 500):
            print(a, b)
            if is_equal(a, b):
                c = 1000 - a - b
                if is_triangle(a, b, c) and is_right_triangle(a, b, c):
                    return a * b * c


print(special_pythagorean_triplet())
