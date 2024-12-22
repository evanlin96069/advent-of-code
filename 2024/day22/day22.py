from collections import defaultdict, deque


data = None

with open("input.txt") as f:
    data = list(map(int, f.read().split('\n')))

def next(n):
    n = ((n << 6) ^ n) & 0xFFFFFF
    n = ((n >> 5) ^ n) & 0xFFFFFF
    n = ((n << 11) ^ n) & 0xFFFFFF
    return n


def part1():
    count = 0
    for n in data:
        for _ in range(2000):
            n = next(n)
        count += n

    print(count)


def part2():
    total = defaultdict(int)
    for n in data:
        seen = set()
        changes = deque(maxlen=4)
        prev = n % 10
        for _ in range(3):
            n = next(n)
            price = n % 10
            changes.append(price - prev)
            prev = price

        for _ in range(1997):
            n = next(n)
            price = n % 10
            changes.append(price - prev)
            seq = tuple(changes)
            if seq not in seen:
                total[tuple(changes)] += price
                seen.add(seq)
            prev = price

    print(max(total.values()))


part1()
part2()
