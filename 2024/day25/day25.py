locks = []
keys = []

with open("input.txt") as f:
    for s in [s.split('\n') for s in f.read().split('\n\n')]:
        c = s[0][0]
        result = []
        for i in range(5):
            result.append(sum([row[i] == '#' for row in s]))
        if c == '#':
            locks.append(result)
        else:
            keys.append(result)

def part1():
    print(sum(all(k+l <= 7 for k, l in zip(key, lock)) for key in keys for lock in locks))


def part2():
    pass


part1()
part2()
