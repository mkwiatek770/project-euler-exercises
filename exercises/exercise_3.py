# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?


def largest_prime_factor():
    largest_prime = 1
    number = 600851475143
    factor = 1
    while factor <= number:
        if number % factor == 0:
            divided = False
            for i in range(2, factor):
                if factor % i == 0:
                    divided = True
                    break
            if not divided:
                largest_prime = factor
                number /= largest_prime
        factor += 2
    return largest_prime

    # for i in range(1, 600851475143, 2):
    #     divided = False
    #     l = 2
    #     while not divided and l < i:
    #         if i % l == 0:
    #             divided = True
    #         l += 1
    #     if not divided:
    #         largest_prime = i

    # return largest_prime


print(largest_prime_factor())
