import re


def sum_part_numbers():
    total = 0
    with open("input.txt") as input:
        data = input.readlines()

    data = [item.strip("\n") for item in data]

    for row in range(len(data)):
        line = data[row]
        digits_in_line = re.finditer(r"(\d+)", line)
        for match_number in digits_in_line:
            start = match_number.start()
            end = match_number.end() - 1
            number = int(match_number.group(0))
            if (
                    find_symbols_up_down(line, start, end)
                    or row > 0 and find_symbols_up_down(data[row - 1], start, end)
                    or row < len(data) - 1 and find_symbols_up_down(data[row + 1], start, end)
            ):
                total += number

    print(total)


def find_symbols_up_down(line, start, end):
    symbols = list(re.finditer(r"([^a-zA-Z0-9.])", line))
    if symbols:
        for symbol in symbols:
            if start - 1 <= symbol.start() <= end + 1:
                return True

    return False


if __name__ == '__main__':
    sum_part_numbers()

