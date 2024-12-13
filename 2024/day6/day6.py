m = None
gx = None
gy = None

with open("input.txt") as f:
    m = list(map(list, f.read().split('\n')))
    for i in range(len(m)):
        for j in range(len(m[0])):
            if m[i][j] == '^':
                gx = i
                gy = j
                break
        if gx is not None:
            break

UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3

path = [[False] * len(m[0]) for _ in range(len(m))]

def part1():
    dir = UP
    x = gx
    y = gy
    while True:
        path[x][y] = True

        nx = x
        ny = y
        if dir == UP:
            nx -= 1
        elif dir == RIGHT:
            ny += 1
        elif dir == DOWN:
            nx += 1
        elif dir == LEFT:
            ny -= 1

        if not (0 <= nx < len(m) and 0 <= ny < len(m[0])):
            break

        if m[nx][ny] == '#':
            dir = (dir + 1) % 4
        else:
            x = nx
            y = ny

    count = sum(sum(row) for row in path)
    print(count)


def part2():
    def run():
        record = set()
        dir = UP
        x = gx
        y = gy
        while True:
            nx = x
            ny = y
            if dir == UP:
                nx -= 1
            elif dir == RIGHT:
                ny += 1
            elif dir == DOWN:
                nx += 1
            elif dir == LEFT:
                ny -= 1

            if not (0 <= nx < len(m) and 0 <= ny < len(m[0])):
                return False

            if m[nx][ny] == '#':
                dir = (dir + 1) % 4
            else:
                x = nx
                y = ny
            if (x, y, dir) in record:
                return True
            record.add((x, y, dir))


    count = 0
    for i in range(len(m)):
        for j in range(len(m[0])):
            if path[i][j] and m[i][j] == '.':
                m[i][j] = '#'
                if run():
                    count += 1
                m[i][j] = '.'
    print(count)


part1()
part2()
