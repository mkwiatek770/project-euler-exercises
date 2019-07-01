
def power_digit_sum(num, exp):
    res = num ** exp
    return sum([int(digit) for digit in str(res)])


if __name__ == "__main__":
    print(power_digit_sum(2, 15))
    
