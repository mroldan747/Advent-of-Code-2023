import re


def sum_part_numbers():
    total = 0
    with open("input.txt") as input:
        data = input.readlines()

    data = [item.strip("\n") for item in data]

    for row in range(len(data)):
        line = data[row]
        symbols_in_line = re.finditer(r"([^a-zA-Z0-9.])", line)
        for match_symbol in symbols_in_line:
            part_numbers = []
            start = match_symbol.start()
            if num := find_symbols_up_down(line, start):
                part_numbers += num
            if row > 0 and (num := find_symbols_up_down(data[row - 1], start)):
                part_numbers += num
            if row < len(data) - 1 and (num := find_symbols_up_down(data[row + 1], start)):
                part_numbers += num

            if len(part_numbers) == 2:
                total += (part_numbers[0] * part_numbers[1])

    print(total)


def find_symbols_up_down(line, start):
    numbers = list(re.finditer(r"(\d+)", line))
    numbers_found = []
    if numbers:
        for num in numbers:
            start_num = num.start()
            end_num = num.end()
            if start_num - 1 <= start <= end_num:
                numbers_found.append(int(num.group(0)))

    return numbers_found


if __name__ == '__main__':
    sum_part_numbers()
