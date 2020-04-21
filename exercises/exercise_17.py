
DIGIT_MAP = {
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine",
    10: "ten",
    11: "eleven",
    12: "twelve",
    20: "twenty",
    30: "thirty",
    40: "forty",
    50: "fifty",
    60: "sixty",
    70: "seventy",
    80: "eighty",
    90: "ninety",
    100: "hundred",
    1000: "thousand",
}


def letter_used(num):
    full_phrase = []

    if num // 1000 >= 1:
        full_phrase.extend([DIGIT_MAP[num // 1000], DIGIT_MAP[1000]])
        num = num - (num // 1000)*1000

    if num // 100 >= 1:
        full_phrase.extend([DIGIT_MAP[num // 100], DIGIT_MAP[100]])
        num = num - (num // 100)*100
        if num > 0:
            full_phrase.append("and")
    if num // 10 >= 1:
        if num in DIGIT_MAP:
            full_phrase.append(DIGIT_MAP[num])
            num = 0
        else:
            full_phrase.append(DIGIT_MAP[int(f"{num // 10}0")])
            num = num - (num // 10)*10
    if num > 0:
        full_phrase.append(DIGIT_MAP[num])
    print(full_phrase)
    return len("".join(full_phrase))


# def letter_used_v2(number):
#     total = sum(DIGIT_MAP[int(d)][1] for d in str(number))
#     if number >= 1000:
#         total += len("thousand")
#         number = number = (number // 1000)*1000
#     if number >= 100:
#         total += len("hundredand")
#     return total


if __name__ == "__main__":
    print(letter_used(1234))
    print(letter_used(342))
    print(letter_used(115))
    print(letter_used(1000))
    print(letter_used(100))

    counter = 0
    for i in range(1, 1001):
        counter += letter_used(i)
    print(counter)

    # Version 2
    # print(letter_used_v2(342))
