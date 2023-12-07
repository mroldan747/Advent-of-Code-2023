import re


def get_lowest_location():
    with open("input.txt") as input:
        data = input.readlines()

    data = [item.strip("\n") for item in data]
    seeds_ranges = re.findall(r"\d+ \d+", data[0])
    # seeds_ranges = [[int(s.split(" ")[0]), int(s.split(" ")[0]) + int(s[1])]for s in seeds_ranges]
    seeds = []
    for seeds_range in seeds_ranges:
        seeds_range = seeds_range.split(" ")
        start = int(seeds_range[0])
        end = start + int(seeds_range[1])
        all_seeds = list(range(start, end))
        seeds += all_seeds


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
                _start = int(maps[0])
                source_range_start = int(maps[1])
                range_length = int(maps[2])
                if source_range_start <= key < (source_range_start + range_length):
                    key = key - source_range_start + destination_start
                    map = False
        locations.append(key)

    print(min(locations))

if __name__ == '__main__':
    get_lowest_location()

