
def find_difference_100_nums():
    return sum((i for i in range(1, 101)))**2 - sum((i**2 for i in range(1, 101)))

