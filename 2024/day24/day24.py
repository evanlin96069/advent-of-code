import re


init_state = None
connections = None

with open("input.txt") as f:
    p1, p2 = f.read().split('\n\n')
    init_state = {l[:3]: int(l[5:])for l in p1.split('\n')}
    connections = list(map(list, re.findall(r"(\w+)\s+(AND|XOR|OR)\s+(\w+)\s+->\s+(\w+)", p2)))

def part1():
    state = init_state.copy()
    for _ in range(len(connections)):
        for in1, op, in2, out in connections:
            if in1 in state and in2 in state and out not in state:
                a = state[in1]
                b = state[in2]
                if op == "AND":
                    state[out] = a & b
                elif op == "OR":
                    state[out] = a | b
                elif op == "XOR":
                    state[out] = a ^ b
    result = 0
    for key in sorted(state)[::-1]:
        if key[0] == 'z':
            result <<= 1
            result |= state[key]
    print(result)


def part2():
    def find(a, gate, b):
        if a is None or b is None:
            return None
        for in1, op, in2, out in connections:
            if op == gate and ((in1 == a and in2 == b) or (in1 == b and in2 == a)):
                return out
        return None


    def swap(a, b):
        for i, (in1, op, in2, out) in enumerate(connections):
            if out == a:
                connections[i][3] = b
            elif out == b:
                connections[i][3] = a


    '''
    Bad solution:
    I just print out the operations, find where `None` occurs, and swap the incorrect ones manually.
    '''
    swap("qjb", "gvw")
    swap("z15", "jgc")
    swap("z22", "drg")
    swap("z35", "jbp")

    bits = max(int(k[1:]) for k in init_state if k[0] == 'x') + 1
    carry = None
    for i in range(bits):
        a = f"x{i:02d}"
        b = f"y{i:02d}"
        xor1 = find(a, "XOR", b)
        print("CARRY =", carry)
        print(a, "XOR", b, "->", xor1)
        and1 = find(a, "AND", b)
        print(a, "AND", b, "->", and1)
        if i != 0:
            xor2 = find(xor1, "XOR", carry)
            print(xor1, "XOR", carry, "->", xor2)
            and2 = find(xor1, "AND", carry)
            print(xor1, "AND", carry, "->", and2)
            carry = find(and1, "OR", and2)
            print(and1, "OR", and2, "->", carry)
        else:
            carry = and1

    incorrect = ["qjb", "gvw", "z15", "jgc", "z22", "drg", "z35", "jbp"]
    print(",".join(sorted(incorrect)))


part1()
part2()
