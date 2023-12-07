import re


def get_lowest_location():
    with open("input.txt") as input:
        data = input.readlines()

    data = [item.strip("\n") for item in data]
    seeds = re.findall(r"\d+", data[0])

    locations = []
    for seed in seeds:
        map = False
        key = int(seed)
        for line in data[2:]:
            if line == "":
                map = False
                continue
            if "map" in line:
                map = True
                continue
            if map:
                maps = line.split(" ")
                destination_start = int(maps[0])
                source_range_start = int(maps[1])
                range_length = int(maps[2])
                if source_range_start <= key < (source_range_start + range_length):
                    key = key - source_range_start + destination_start
                    map = False
        locations.append(key)

    print(min(locations))

if __name__ == '__main__':
    get_lowest_location()

