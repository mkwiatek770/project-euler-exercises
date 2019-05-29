

def is_prime(num):
    for i in range(2, num // 2 + 1):
        if num % i == 0:
            return False
    return True


def sum_primes_below(bound=2000000):
    sum_of_primes = 2
    for i in range(3, bound, 2):
        if is_prime(i):
            sum_of_primes += i
    return sum_of_primes


if __name__ == "__main__":
    print(sum_primes_below(bound=10))
    print(sum_primes_below(bound=20))
