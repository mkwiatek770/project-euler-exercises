# The following iterative sequence is defined for the set of positive integers:
# n → n/2 (n is even)
# n → 3n + 1 (n is odd)
# Using the rule above and starting with 13, we generate the following sequence:
# 13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
# It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.
# Which starting number, under one million, produces the longest chain?

def colatz_count(starting):
    num = starting
    counter = 1
    while num != 1:
        if num % 2 == 0:
            num /= 2
        else:
            num = 3*num + 1
        counter += 1
    return counter

def find_highest_colatz(border):
    highest_count = 1
    highest_num = 1
    for i in range(2, border):
        res = colatz_count(i)
        if res > highest_count:
            highest_num = i
            highest_count = res
            print(i)
    return highest_num

if __name__ == "__main__":
    print(find_highest_colatz(14))
