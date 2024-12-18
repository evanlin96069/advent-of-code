from collections import deque


data = None
w = h = None
filename = "input.txt"
with open(filename) as f:
    data = [tuple(map(int, l.split(',')))[::-1] for l in f.read().split('\n')]
    h = max([x for x, y in data]) + 1
    w = max([y for x, y in data]) + 1


def bfs(grid):
    h = len(grid)
    w = len(grid[0])

    if grid[0][0] == 1 or grid[h-1][w-1] == 1:
        return -1, []

    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    queue = deque([(0, 0)])

    parent = {}
    parent[(0, 0)] = None

    visited = set()
    visited.add((0, 0))

    while queue:
        x, y = queue.popleft()

        if x == h - 1 and y == w - 1:
            path = []
            pos = (x, y)
            while pos is not None:
                path.append(pos)
                pos = parent[pos]
            return path[::-1]

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if (0 <= nx < h and 0 <= ny < w and
                grid[nx][ny] == 0 and
                (nx, ny) not in visited):
                queue.append((nx, ny))
                visited.add((nx, ny))
                parent[(nx, ny)] = (x, y)

    return None


def part1():
    size = 1024 if filename == "input.txt" else 12
    grid = [[0] * w for _ in range(h)]
    for x, y in data[:size]:
        grid[x][y] = 1
    print(len(bfs(grid)) - 1)


def part2():
    grid = [[0] * w for _ in range(h)]
    path = bfs(grid)
    for i, (x, y) in enumerate(data):
        grid[x][y] = 1
        if (x, y) not in path:
            continue
        path = bfs(grid)
        if path is None:
            print(",".join(map(str,data[i][::-1])))
            return


part1()
part2()
