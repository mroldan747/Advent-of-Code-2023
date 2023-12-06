
DATA = [{"t": 59, "r": 597}, {"t": 79, "r": 1234}, {"t": 65, "r": 1032}, {"t": 75, "r": 1328}]


def get_possibilities():
    total = 1
    for input in DATA:
        possible = 0
        for time in range(1, input["t"] + 1):
            if (time * (input["t"] - time)) > input["r"]:
                possible += 1
        total *= possible

    print(total)

if __name__ == '__main__':
    get_possibilities()

