from functools import cmp_to_key


rules = None
updates = None

with open("input.txt") as f:
    rules, updates = (part.split('\n') for part in f.read().split('\n\n'))
    rules = [list(map(int, rule.split('|'))) for rule in rules]
    updates = [list(map(int, update.split(','))) for update in updates]


def compare(a, b):
    for rule in rules:
        if (a in rule) and (b in rule):
            if a == rule[0]:
                return -1
            return 1
    return 0


def part1():
    count = 0
    for update in updates:
        correct = sorted(update, key=cmp_to_key(compare))
        if correct == update:
            count += correct[len(update) // 2]

    print(count)


def part2():
    count = 0
    for update in updates:
        correct = sorted(update, key=cmp_to_key(compare))
        if correct != update:
            count += correct[len(update) // 2]

    print(count)


part1()
part2()
