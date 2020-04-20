
DIGIT_MAP = {
            1: ("one", 3),
            2: ("two", 3),
            3: ("three", 5),
            4: ("four", 4),
            5: ("five", 5),
            6: ("six", 3),
            7: ("seven", 5),
            8: ("eight", 5),
            9: ("nine", 5),
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
            100: ("hundred and", 10),
            1000: ("thousand and", 11),
        }


def letter_used(num):
    digits = [int(str(d)) for d in str(num)]
    
    counter = 0
    for digit in digits:
        counter += DIGIT_MAP[digit][1]
    print(counter)


if __name__ == "__main__":
    letter_used(1234)
