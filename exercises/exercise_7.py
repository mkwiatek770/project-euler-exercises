
def find_nth_prime(n):
    prime_nums = 0
    last_prime_num = 0
    num = 2
    while prime_nums < n:
        divisible = False
        for i in range(2, num + 1):
            if num % i == 0 and num != i:
                divisible = True
        if not divisible:
            last_prime_num = num
            prime_nums += 1
        num += 1
        print(prime_nums)
    return last_prime_num

if __name__ == '__main__':

    print(find_nth_prime(2))
    print(find_nth_prime(3))
    print(find_nth_prime(4))
    print(find_nth_prime(6))
    print(find_nth_prime(10001))


