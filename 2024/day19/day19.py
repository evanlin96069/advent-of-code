from functools import lru_cache


patterns = None
data = None

with open("input.txt") as f:
    t1, t2 = f.read().split('\n\n')
    patterns = t1.split(', ')
    data = t2.split('\n')

def part1():
    def search(s):
        if len(s) == 0:
            return True

        for pattern in patterns:
            if (s.startswith(pattern) and
                search(s[len(pattern):])):
                    return True

        return False

    print(sum([search(s) for s in data]))


def part2():
    @lru_cache
    def search(s):
        if len(s) == 0:
            return 1

        return sum([search(s[len(pattern):]) if s.startswith(pattern) else 0 for pattern in patterns])


    print(sum([search(s) for s in data]))


part1()
part2()
