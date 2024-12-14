import copy

robots = []
# w = 11
# h = 7
w = 101
h = 103

with open("input.txt") as f:
    for line in f.read().split('\n'):
        p = tuple(map(int, line.split("p=")[1].split(" ")[0].split(",")))
        v = tuple(map(int, line.split("v=")[1].split(",")))
        p = [p[1], p[0]]
        v = (v[1], v[0])
        robots.append((p, v))


def part1():
    data = copy.deepcopy(robots)
    for _ in range(100):
        for p, v in data:
            p[0] = (p[0] + v[0]) % h
            p[1] = (p[1] + v[1]) % w

    room = [[0 for i in range(w)] for j in range(h)]
    for p, v in data:
        room[p[0]][p[1]] += 1

    factor = 1
    for i in range(2):
        for j in range(2):
            count = 0
            dx = (h//2 + 1) * i
            dy = (w//2 + 1) * j
            for x in range(dx, dx + h//2):
                for y in range(dy, dy * j + w//2):
                    count += room[x][y]
            factor *= count

    print(factor)


def part2():
    data = copy.deepcopy(robots)
    for step in range(1, 10000):
        for p, v in data:
            p[0] = (p[0] + v[0]) % h
            p[1] = (p[1] + v[1]) % w

        room = [[0 for i in range(w)] for j in range(h)]
        for p, v in data:
            room[p[0]][p[1]] += 1
        print(f"Step: {step}")
        for row in room:
            print("".join('*' if cell != 0 else '.' for cell in row))


part1()
part2()

# python day14.py > out.txt
# grep -Fn "******" out.txt
# sed -n "677550, 677700p" out.txt | less
