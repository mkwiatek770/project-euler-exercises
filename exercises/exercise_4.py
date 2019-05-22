
# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
# Find the largest palindrome made from the product of two 3-digit numbers.


def find_largest_palindrome_product():
    a = 999
    b = 999
    largest_res = 1
    for a in range(999, 99, -1):
        for b in range(999, 99, -1):
            res = a * b
            if str(res) == str(res)[::-1] and res > largest_res:
                largest_res = res
    return largest_res


print(find_largest_palindrome_product())
