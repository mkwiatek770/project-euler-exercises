
digits = {
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
            100: "one hundred",
            1000: "one thousand"
        }


def letter_used(num):
    digits = [str(d) for d in str(num)]
    print(digits)

if __name__ == "__main__":
    letter_used(1234)
