from collections import Counter


l1 = []
l2 = []

with open("input.txt") as f:
    for line in f.read().split('\n'):
        l, r = map(int, line.split())
        l1.append(l)
        l2.append(r)


def part1():
    s1 = sorted(l1)
    s2 = sorted(l2)

    dist = 0
    for i in range(len(s1)):
        dist += abs(s1[i] - s2[i])

    print(dist)


def part2():
    l2c = Counter(l2)

    score = 0
    for n in l1:
        score += n * l2c[n]

    print(score)


part1()
part2()
