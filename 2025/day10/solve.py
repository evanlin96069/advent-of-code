import numpy as np
from scipy.optimize import linprog


data = []

with open("input.txt") as f:
    for l in f.read().strip('\n').split('\n'):
        l = l.split(' ')[1:]
        buttons = []
        for s in l[:-1]:
            buttons.append(tuple(map(int, s[1:-1].split(','))))
        counters = tuple(map(int, l[-1][1:-1].split(',')))
        data.append((buttons, counters))


def part1():
    # in ika
    pass


def part2():
    count = 0
    for buttons, counters in data:
        a = np.zeros((len(buttons), len(counters)))
        for i, button in enumerate(buttons):
            for index in button:
                a[i][index] = 1
        a = a.T
        b = np.array(counters)
        ans = linprog([1] * len(buttons), A_eq=a, b_eq=b, bounds=(0, None), method='highs', integrality=1)
        count += round(ans.fun)
    print(count)


part1()
part2()
