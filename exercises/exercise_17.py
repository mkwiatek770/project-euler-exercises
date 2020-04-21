
DIGIT_MAP = {
            1: ("one", 3),
            2: ("two", 3),
            3: ("three", 5),
            4: ("four", 4),
            5: ("five", 4),
            6: ("six", 3),
            7: ("seven", 5),
            8: ("eight", 5),
            9: ("nine", 4),
            10: ("ten", 3),
            11: ("eleven", 6),
            12: ("twelve", 6),
            20: ("twenty", 6),
            30: ("thirty", 6),
            40: ("fourty", 6),
            50: ("fifty", 5),
            60: ("sixty", 5),
            70: ("seventy", 7),
            80: ("eighty", 6),
            90: ("ninety", 6),
            100: ("hundred", 7),
            1000: ("thousand", 8),
        }


def letter_used(num):
    counter = 0
    full_phrase = ""

    if num // 1000 >= 1:
        thousands = DIGIT_MAP[num // 1000]
        thousand = DIGIT_MAP[1000]
        
        full_phrase += thousands[0]
        full_phrase += thousand[0]

        counter += thousands[1]
        counter += thousands[1]

        num = num - (num // 1000)*1000

    if num // 100 >= 1:
        hundreds = num // 100
        counter += DIGIT_MAP[hundreds][1]
        counter += DIGIT_MAP[100][1]
        num = num - (num // 100)*100
        if num > 0:
            counter += len("and")
    if num // 10 >= 1:
        if num in DIGIT_MAP:
            counter += DIGIT_MAP[num][1]
            num = 0
        else:
            decimal = num // 10
            counter += DIGIT_MAP[int(str(decimal) + '0')][1]
            num = num - (num // 10)*10
    if num > 0:
        counter += DIGIT_MAP[num][1]
    print(full_phrase)
    return counter

def letter_used_v2(number):
    total = sum(DIGIT_MAP[int(d)][1] for d in str(number))
    if number >= 1000:
        total += len("thousand")
        number = number = (number // 1000)*1000
    if number >= 100:
        total += len("hundredand")
    return total


if __name__ == "__main__":
    print(letter_used(1234))
    print(letter_used(342))
    print(letter_used(115))
    print(letter_used(1000))
    print(letter_used(100))

    #counter = 0
    #for i in range(1, 1001):
    #    counter += letter_used(i)
    #print(counter)

    # Version 2
    print(letter_used_v2(342))

