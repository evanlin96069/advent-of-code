m = None
with open("input.txt") as f:
    m = f.read().split("\n")

def get(x, y):
    if 0 <= x < len(m) and 0 <= y < len(m[x]):
        return m[x][y]
    return None

def part1():
    count = 0

    for i in range(len(m)):
        for j in range(len(m[i])):
            if m[i][j] != 'X':
                continue

            if (get(i, j+1) == 'M' and
                get(i, j+2) == 'A' and
                get(i, j+3) == 'S'):
                   count += 1

            if (get(i, j-1) == 'M' and
                get(i, j-2) == 'A' and
                get(i, j-3) == 'S'):
                   count += 1

            if (get(i+1, j) == 'M' and
                get(i+2, j) == 'A' and
                get(i+3, j) == 'S'):
                   count += 1

            if (get(i-1, j) == 'M' and
                get(i-2, j) == 'A' and
                get(i-3, j) == 'S'):
                   count += 1

            if (get(i+1, j+1) == 'M' and
                get(i+2, j+2) == 'A' and
                get(i+3, j+3) == 'S'):
                   count += 1

            if (get(i+1, j-1) == 'M' and
                get(i+2, j-2) == 'A' and
                get(i+3, j-3) == 'S'):
                   count += 1

            if (get(i-1, j+1) == 'M' and
                get(i-2, j+2) == 'A' and
                get(i-3, j+3) == 'S'):
                   count += 1

            if (get(i-1, j-1) == 'M' and
                get(i-2, j-2) == 'A' and
                get(i-3, j-3) == 'S'):
                   count += 1

    print(count)


def part2():
    count = 0

    for i in range(1, len(m)-1):
        for j in range(1, len(m[i])-1):
            if m[i][j] != 'A':
                continue

            tl = get(i-1, j-1)
            tr = get(i-1, j+1)
            bl = get(i+1, j-1)
            br = get(i+1, j+1)

            if (((tl == 'M' or tl == 'S') and (br == 'M' or br == 'S') and tl != br) and
                ((tr == 'M' or tr == 'S') and (bl == 'M' or bl == 'S') and tr != bl)):
               count += 1

    print(count)


part1()
part2()
