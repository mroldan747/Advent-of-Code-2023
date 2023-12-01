import re


def sum_calibration_values():
    with open("./Day1/input.txt") as input:
        lines = input.readlines()
    calibration_values = []
    for line in lines:
        digits = re.findall(r'\d{1}', line)
        num = digits[0] + digits[-1]
        calibration_values.append(int(num))

    print(sum(calibration_values))


if __name__ == '__main__':
    sum_calibration_values()
