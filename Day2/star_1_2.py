import re
import math

MAX_VALUES = {"blue": 14, "green": 13, "red": 12}


def get_lines():
    with open("input.txt") as input:
        lines = input.readlines()
    return lines


def get_max_set_values(sets):
    max_set_values = {"blue": 0, "green": 0, "red": 0}
    for set in sets:
        color_cubes = set.strip().split(",")
        for cubes in color_cubes:
            values = cubes.strip().split(" ")
            if max_set_values[values[1]] < int(values[0]):
                max_set_values[values[1]] = int(values[0])

    return max_set_values


def calc_possible_games():
    total = 0
    for line in get_lines():
        possible = True
        id = re.search(r"Game (\d+)", line).group(1)
        sets = line.split(":")[1].split(";")
        max_set_values = get_max_set_values(sets)
        for k, v in max_set_values.items():
            if MAX_VALUES[k] < v:
                possible = False
                break
        if possible:
            total += int(id)

    print(total)


def calc_fewest_numbers_of_cubes():
    total = 0
    for line in get_lines():
        sets = line.split(":")[1].split(";")
        max_set_values = get_max_set_values(sets)
        power = math.prod(max_set_values.values())
        total += power

    print(total)


if __name__ == '__main__':
    calc_possible_games()
    calc_fewest_numbers_of_cubes()
