import re


code = None

with open("input.txt") as f:
    code = f.read()


def part1():
    exprs = [x[4:-1].split(',') for x in re.findall(r'mul\(\d+,\d+\)', code)]
    print(sum(int(x) * int(y) for x, y in exprs))


def part2():
    exprs = [x[4:-1].split(',') for x in re.findall(r"(?s)don't\(\).*?do\(\)|mul\(\d+,\d+\)", code) if x.startswith('mul')]
    print(sum(int(x) * int(y) for x, y in exprs))



part1()
part2()
