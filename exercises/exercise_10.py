primes = [2]
def is_prime(num):
    for p in primes:
        if num % p == 0:
            return False
        if p * 2 > num:
            break
    primes.append(num)
    print(num)
    return True

def sum_primes_below(bound=10):
    for i in range(3, bound, 2):
        is_prime(i)
    sum_primes = sum(primes)
    primes = [2]
    return sum_primes
            

if __name__ == "__main__":
    print(sum_primes_below(bound=1000000))
