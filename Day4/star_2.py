import re


def sum_part_numbers():
    with open("input.txt") as input:
        data = input.readlines()

    data = [item.strip("\n") for item in data]
    instances = {}
    for line in data:
        card = int(re.search(r"Card\s+(\d+)", line).group(1))
        instances[card] = instances[card] + 1 if instances.get(card) else 1

        sets = line.split(":")[1].split("|")
        winning_num = sets[0].strip().split(" ")
        my_num = sets[1].strip().split(" ")
        matches = 0
        for num in my_num:
            if num != "" and num in winning_num:
                matches += 1

        if matches:
            for match in range(card + 1, card + matches + 1):
                instances[match] = instances[match] + instances[card] if instances.get(match) else instances[card]

    print(sum(instances.values()))


if __name__ == '__main__':
    sum_part_numbers()

