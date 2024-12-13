import re


data = []

with open("input.txt") as f:
    for block in f.read().split('\n\n'):
        pattern = r'X[+=](\d+), Y[+=](\d+)'
        matches = re.findall(pattern, block)
        data.append([tuple(map(int, match)) for match in matches])

def solve(a, b, p):
    det = a[0] * b[1] - b[0] * a[1]
    dx = p[0] * b[1] - b[0] * p[1]
    dy = a[0] * p[1] - p[0] * a[1]

    x = dx / det
    y = dy / det

    if x.is_integer() and y.is_integer():
        return int(x * 3 + y * 1)

    return 0


def part1():
    print(sum(solve(a, b, p) for a, b, p in data))


def part2():
    print(sum(solve(a, b, (p[0]+10000000000000, p[1]+10000000000000)) for a, b, p in data))


part1()
part2()
