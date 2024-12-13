from itertools import product
from functools import lru_cache


data = []

with open("input.txt") as f:
    for line in f.read().split('\n'):
        a, b = line.split(': ')
        a = int(a)
        b = tuple(map(int, b.split(' ')))
        data.append((a, b))

@lru_cache(typed=False)
def compute(ops, nums):
    if not ops:
        return nums[0]

    s = compute(ops[:-1], nums[:-1])
    num = nums[-1]
    op = ops[-1]

    if op == 0:
        s += num
    elif op == 1:
        s *= num
    else:
        s = s * 10 ** len(str(num)) + num

    return s


part1_pass = set()

def part1():
    total = 0
    for i, (goal, nums) in enumerate(data):
        for ops in product([0, 1], repeat=len(nums)-1):
            if compute(ops, nums) == goal:
                part1_pass.add(i)
                total += goal
                break

    print(total)


def part2():
    total = 0
    for i, (goal, nums) in enumerate(data):
        if i in part1_pass:
            total += goal
            continue
        for ops in product([0, 1, 2], repeat=len(nums)-1):
            if compute(ops, nums) == goal:
                total += goal
                break

    print(total)


part1()
part2()
