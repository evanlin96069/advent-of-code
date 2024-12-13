import string


keys = string.ascii_lowercase + string.ascii_uppercase + string.digits
data = {key: [] for key in keys}

city = None

with open("input.txt") as f:
    city = list(map(list, f.read().split('\n')))
    for i in range(len(city)):
        for j in range(len(city[0])):
            if city[i][j] != '.':
                data[city[i][j]].append((i, j))


def check(p):
    return 0 <= p[0] < len(city) and 0 <= p[1] < len(city[0])


def part1():
    s = set()

    for k, v in data.items():
        if len(v) < 2:
            continue
        for i in range(len(v)):
            for j in range(i+1, len(v)):
                p1 = v[i]
                p2 = v[j]
                dx = p1[0] - p2[0]
                dy = p1[1] - p2[1]
                p1 = p1[0] + dx, p1[1] + dy
                p2 = p2[0] - dx, p2[1] - dy
                if check(p1):
                    s.add(p1)
                if check(p2):
                    s.add(p2)

    print(len(s))


def part2():
    s = set()

    for k, v in data.items():
        if len(v) < 2:
            continue
        for i in range(len(v)):
            for j in range(i+1, len(v)):
                p1 = v[i]
                p2 = v[j]
                dx = p1[0] - p2[0]
                dy = p1[1] - p2[1]
                while check(p1):
                    s.add(p1)
                    p1 = (p1[0] + dx, p1[1] + dy)
                while check(p2):
                    s.add(p2)
                    p2 = (p2[0] - dx, p2[1] - dy)

    print(len(s))


part1()
part2()
