import regex as re

DIGITS = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}

def sum_calibration_values():
    with open("input.txt") as input:
        lines = input.readlines()
    calibration_values = []
    for line in lines:
        pattern = "|".join(DIGITS.keys())
        digits = re.findall(r"\d{1}|" + pattern, line, overlapped=True)
        digits = [DIGITS[digit] if digit in DIGITS else digit for digit in digits]
        num = digits[0] + digits[-1]
        calibration_values.append(int(num))

    print(sum(calibration_values))


if __name__ == '__main__':
    sum_calibration_values()
