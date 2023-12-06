

def get_possibilities():
    race_time = 59796575
    record = 597123410321328
    possible = 0
    for time in range(1, race_time + 1):
        if (time * (race_time - time)) > record:
            possible += 1
    print(possible)

if __name__ == '__main__':
    get_possibilities()

