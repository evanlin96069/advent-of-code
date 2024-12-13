s = None
data = None

with open("input.txt") as f:
    s = f.read()
    data = []
    index = 0
    for i, c in enumerate(s):
        if i % 2 == 0:
            data += [index] * int(c)
            index += 1
        else:
            data += [None] * int(c)


def checksum(d):
    r = 0
    for i, c in enumerate(d):
        if c is not None:
            r += c * i
    return r


def part1():
    start = 0
    d = data.copy()
    end = len(d) - 1
    while True:
        while start < len(d) and d[start] is not None:
            start += 1
        while end >= 0 and d[end] is None:
            end -= 1
        if end <= start:
            break

        d[start], d[end] = d[end], d[start]

    print(checksum(d))


def part2():
    d = data.copy()

    end = len(d) - 1

    cache = []

    while end >= 0:
        while end >= 0 and d[end] is None:
            end -= 1
        if end < 0:
            break
        size = 0
        i = 0
        while end - i >= 0 and d[end-i] == d[end]:
            size += 1
            i += 1

        start = None
        oob = False
        for i, (index, space) in enumerate(cache):
            if index >= end:
                oob = True
                break
            if size <= space:
                start = index
                cache[i][0] += size
                cache[i][1] -= size
                break

        if start is None and not oob:
            if cache:
                start = cache[-1][0] + cache[-1][1]
            else:
                start = 0

            while start < end:
                while start < end and d[start] is not None:
                    start += 1
                if start >= end:
                    break

                space = 0
                i = 0
                while start + i < end and d[start+i] is None:
                    space += 1
                    i += 1

                if size <= space:
                    break
                cache.append([start, space])
                start += space

        if start and start < end:
            for i in range(size):
                d[start+i], d[end-i] = d[end-i], d[start+i]
        end -= size

    print(checksum(d))


part1()
part2()
