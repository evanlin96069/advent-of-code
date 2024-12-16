import copy


maze = None
moves = None
px, py = None, None

with open("input.txt") as f:
    s = f.read()
    maze, moves = s.split("\n\n")
    moves = "".join(moves.split("\n"))
    maze = list(map(list, maze.split("\n")))
    for i in range(len(maze)):
        for j in range(len(maze[0])):
            if maze[i][j] == "@":
                px, py = i, j
                maze[i][j] = "."
                break
        if px is not None:
            break

dirs = {
    "v" : (1, 0),
    "^" : (-1, 0),
    ">" : (0, 1),
    "<" : (0, -1),
}

def part1():
    x, y = px, py
    data = copy.deepcopy(maze)
    for m in moves:
        dx, dy = dirs[m]
        nx, ny = x+dx, y+dy
        while data[nx][ny] == "O":
            nx += dx
            ny += dy
        if data[nx][ny] == ".":
            data[nx][ny] = "O"
            data[x+dx][y+dy] = "."
            x, y = x+dx, y+dy

    n = 0
    for i in range(len(data)):
        for j in range(len(data[0])):
            if data[i][j] == "O":
                n += 100 * i + j

    print(n)


def part2():
    x, y = px, py*2
    data = []

    def check(x, y, dx):
        if data[x+dx][y] == ".":
            return True
        if data[x+dx][y] == "#":
            return False
        if data[x+dx][y] == "[":
            return check(x+dx, y, dx) and check(x+dx, y+1, dx)
        if data[x+dx][y] == "]":
            return check(x+dx, y, dx) and check(x+dx, y-1, dx)


    def move(x, y, dx):
        if data[x+dx][y] == "[":
            move(x+dx, y, dx)
            move(x+dx, y+1, dx)
        if data[x+dx][y] == "]":
            move(x+dx, y, dx)
            move(x+dx, y-1, dx)

        data[x][y], data[x+dx][y] = data[x+dx][y], data[x][y]


    for i in range(len(maze)):
        row = ""
        for j in range(len(maze[0])):
            if maze[i][j] == "O":
                row += "[]"
            else:
                row += maze[i][j] * 2
        data.append(list(row))

    for m in moves:
        dx, dy = dirs[m]
        if m in "<>":
            ny = y+dy
            while data[x][ny] in "[]":
                ny += dy
            if data[x][ny] == ".":
                data[x].insert(y+dy, data[x].pop(ny))
                y += dy
        else:
            if check(x, y, dx):
                move(x, y, dx)
                x += dx

    n = 0
    for i in range(len(data)):
        for j in range(len(data[0])):
            if data[i][j] == "[":
                n += 100 * i + j

    print(n)


part1()
part2()
