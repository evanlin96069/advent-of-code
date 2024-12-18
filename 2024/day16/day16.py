import heapq


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

def bfs(maze):
    dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    pq = [(0, (start,), 0)]  # (score, path, dir)
    best_scores = { (start, 0): 0 } # { (pos, dir): score }
    best_tiles = set()
    best_score = None

    while pq:
        score, path, di = heapq.heappop(pq)
        x, y = path[-1]

        if maze[x][y] == 'E':
            best_tiles |= {*path}
            best_score = score
            continue

        if best_score is None or score < best_score:
            for d, (dx, dy) in enumerate(dirs):
                if dirs[di][0] + dirs[d][0] == 0 and dirs[di][1] + dirs[d][1] == 0:
                    continue

                nx, ny = x + dx, y + dy
                if maze[nx][ny] == '#':
                    continue

                new_score = score + 1
                if di != d:
                    new_score += 1000

                state = ((x, y), d)
                if best_scores.get(state, new_score + 1) >= new_score:
                    best_scores[state] = new_score
                    heapq.heappush(pq, (new_score, path + ((nx, ny),), d))

    return best_score, best_tiles


best_score, tiles = bfs(maze)

def part1():
    print(best_score)


def part2():
    print(len(tiles))


part1()
part2()

