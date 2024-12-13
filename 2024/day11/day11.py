from collections import Counter


data = None

with open("input.txt") as f:
    data = list(map(int, f.read().split(' ')))


def blink(data, blinks):
    stones = Counter(data)
    for _ in range(blinks):
        curr = Counter()
        for n, count in stones.items():
            s = str(n)
            l = len(s)
            if n == 0:
                curr[1] += count
            elif l % 2 == 0:
                curr[int(s[:l//2])] += count
                curr[int(s[l//2:])] += count
            else:
                curr[n * 2024] += count
        stones = curr

    return sum(stones.values())


def part1():
    print(blink(data, 25))


def part2():
    print(blink(data, 75))


part1()
part2()
