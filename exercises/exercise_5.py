# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?


def find_smallest_div():
    num = 20
    while True:
        divided_by_all = True
        for i in range(1, 21):
            if num % i != 0:
                divided_by_all = False
        if divided_by_all:
            return num
        num += 20



