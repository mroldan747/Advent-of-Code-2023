
def sum_part_numbers():
    total = 0
    with open("input.txt") as input:
        data = input.readlines()

    data = [item.strip("\n") for item in data]

    for line in data:
        total_line = 0
        sets = line.split(":")[1].split("|")
        winning_num = sets[0].strip().split(" ")
        my_num = sets[1].strip().split(" ")
        matches = 0
        for num in my_num:
            if num != "" and num in winning_num:
                matches += 1

        if matches:
            total_line = 2 ** (matches - 1)

        total += total_line

    print(total)


if __name__ == '__main__':
    sum_part_numbers()

