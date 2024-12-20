maze = None
start = None

with open("input.txt") as f:
    maze = f.read().split('\n')
    for i in range(len(maze)):
        for j in range(len(maze[0])):
            if maze[i][j] == 'S':
                start = i, j
                break
        if start is not None:
            break


def create_grid(maze):
    grid = [[None] * len(maze[0]) for _ in range(len(maze))]

    dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    step = 1
    x, y = start
    while maze[x][y] != 'E':
        grid[x][y] = step
        step += 1
        for dx, dy in dirs:
            nx = x + dx
            ny = y + dy
            if maze[nx][ny] != '#' and grid[nx][ny] is None:
                x = nx
                y = ny
                break
    grid[x][y] = step

    return grid


grid = create_grid(maze)

def get_saves(cheat_steps, min_save=100):
    count = 0
    for x1 in range(1, len(grid) - 1):
        for y1 in range(1, len(grid[0]) - 1):
            if grid[x1][y1] is None:
                continue

            for x2 in range(max(1, x1 - cheat_steps), min(len(grid) - 1, x1 + cheat_steps + 1)):
                for y2 in range(max(1, y1 - cheat_steps), min(len(grid[0]) - 1, y1 + cheat_steps + 1)):
                    if grid[x2][y2] is None:
                        continue
                    dist = abs(x1 - x2) + abs(y1 - y2)
                    if dist <= cheat_steps and grid[x1][y1] - grid[x2][y2] - dist >= min_save:
                            count += 1

    return count


def part1():
    print(get_saves(2))


def part2():
    print(get_saves(20))


part1()
part2()
