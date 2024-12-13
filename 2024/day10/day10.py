data = None
w = h = None

with open("input.txt") as f:
    data = [list(map(int, r)) for r in f.read().split('\n')]
    w = len(data[0])
    h = len(data)

def part1():
    def search(point, dst, x, y):
        c = data[x][y]
        if c == 9:
            if (x, y) not in dst:
                dst.add((x, y))
                point[0] += 1
            return
        if x + 1 < h and data[x+1][y] == c+1:
            search(point, dst, x+1, y)
        if x - 1 >= 0 and data[x-1][y] == c+1:
            search(point, dst, x-1, y)
        if y + 1 < w and data[x][y+1] == c+1:
            search(point, dst, x, y+1)
        if y - 1 >= 0 and data[x][y-1] == c+1:
            search(point, dst, x, y-1)

    point = [0]
    for i in range(h):
        for j in range(w):
            dst = set()
            if data[i][j] == 0:
                search(point, dst, i, j)
    print(point[0])


def part2():
    def search(point, x, y):
        c = data[x][y]
        if c == 9:
            point[0] += 1
            return
        if x + 1 < h and data[x+1][y] == c+1:
            search(point, x+1, y)
        if x - 1 >= 0 and data[x-1][y] == c+1:
            search(point, x-1, y)
        if y + 1 < w and data[x][y+1] == c+1:
            search(point, x, y+1)
        if y - 1 >= 0 and data[x][y-1] == c+1:
            search(point, x, y-1)

    point = [0]
    for i in range(h):
        for j in range(w):
            if data[i][j] == 0:
                search(point, i, j)
    print(point[0])


part1()
part2()
