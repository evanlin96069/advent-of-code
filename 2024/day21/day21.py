from functools import cache


data = None

with open("input.txt") as f:
    data = f.read().split('\n')

num_pad = {
    '7': (0, 0),
    '8': (0, 1),
    '9': (0, 2),
    '4': (1, 0),
    '5': (1, 1),
    '6': (1, 2),
    '1': (2, 0),
    '2': (2, 1),
    '3': (2, 2),
    '0': (3, 1),
    'A': (3, 2),
}

dir_pad = {
    '^': (0, 1),
    'A': (0, 2),
    '<': (1, 0),
    'v': (1, 1),
    '>': (1, 2),
}

dirs = {
    '^': (-1, 0),
    'v': (1, 0),
    '>': (0, 1),
    '<': (0, -1),
}

@cache
def seq(s, depth=2, numpad=True, curr='A'):
    if len(s) == 0:
        return 0

    pad = num_pad if numpad else dir_pad

    x, y = pad[curr]
    nx, ny = pad[s[0]]
    dx = nx - x
    dy = ny - y

    mv1 = ('v' if dx > 0 else '^') * abs(dx)
    mv2 = ('>' if dy > 0 else '<') * abs(dy)

    min_len = None
    if depth > 0:
        for p in [mv1 + mv2, mv2 + mv1]:
            cx, cy = x, y
            invalid = False
            for c in p:
                dx, dy = dirs[c]
                cx += dx
                cy += dy
                if (cx, cy) not in pad.values():
                    invalid = True
                    break
            if not invalid:
                length = seq(p + 'A', depth - 1, False)
                if min_len is None:
                    min_len = length
                else:
                    min_len = min(min_len, length)
    else:
        min_len = len(mv1 + mv2 + 'A')
    return min_len + seq(s[1:], depth, numpad, s[0])


def part1():
    print(sum(seq(s) * int(s[:3]) for s in data))


def part2():
    print(sum(seq(s, 25) * int(s[:3]) for s in data))


part1()
part2()
