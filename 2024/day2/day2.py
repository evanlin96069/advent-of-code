reports = None

with open("input.txt") as f:
    reports = [list(map(int, line.split())) for line in f.read().split('\n')]


def is_safe(levels):
    diffs = [i - j for i, j in zip(levels, levels[1:])]
    if all(diff > 0 for diff in diffs) or all(diff < 0 for diff in diffs):
        return all(1 <= abs(diff) <= 3 for diff in diffs)
    return False


def part1():
    count = sum([is_safe(levels) for levels in reports])
    print(count)


def part2():
    def is_safe_with_tolerate(levels):
        if is_safe(levels):
            return True
        for i in range(len(levels)):
            if is_safe(levels[:i] + levels[i + 1:]):
                return True

        return False

    count = sum([is_safe_with_tolerate(levels) for levels in reports])
    print(count)

part1()
part2()
