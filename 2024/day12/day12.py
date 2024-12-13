import copy


region = None
w = h = None

with open("input.txt") as f:
    region = list(map(list, f.read().split('\n')))
    w = len(region[0])
    h = len(region)

def check(x, y):
    return 0 <= x < w and 0 <= y < h


def part1():
    dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    def flood(data, x, y, pos, perimeter):
        if (x, y) in pos:
            return

        c = data[x][y]
        data[x][y] = None
        pos.append((x, y))

        perimeter[0] += 4
        for dx, dy in dirs:
            if (x+dx, y+dy) in pos:
                perimeter[0] -= 2

        for dx, dy in dirs:
            if check(x+dx, y+dy) and data[x+dx][y+dy] == c:
                flood(data, x+dx, y+dy, pos, perimeter)

    price = 0
    data = copy.deepcopy(region)
    for i in range(h):
        for j in range(w):
            if data[i][j] is not None:
                pos = []
                perimeter = [0]
                flood(data, i, j, pos, perimeter)
                price += len(pos) * perimeter[0]

    print(price)


def part2():
    dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    corners = [(-0.5, -0.5), (-0.5, 0.5), (0.5, -0.5), (0.5, 0.5)]

    def flood(data, x, y, pos, vertices):
        if (x, y) in pos:
            return

        c = data[x][y]
        data[x][y] = None
        pos.append((x, y))

        for dx, dy in corners:
            if (x+dx, y+dy) in vertices and (
                (int(x+dx+dx), int(y+dy+dy)) not in pos
                or (x, int(y+dy+dy)) in pos
                or (x, int(y+dy+dy)) in pos
            ):
                    vertices.remove((x+dx, y+dy))
            else:
                vertices.append((x+dx, y+dy))

        for dx, dy in dirs:
            if check(x+dx, y+dy) and data[x+dx][y+dy] == c:
                flood(data, x+dx, y+dy, pos, vertices)

    price = 0
    data = copy.deepcopy(region)
    for i in range(h):
        for j in range(w):
            if data[i][j] is not None:
                pos = []
                vertices = []
                flood(data, i, j, pos, vertices)
                price += len(pos) * len(vertices)
    print(price)


part1()
part2()
