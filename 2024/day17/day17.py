import copy


regs = []
prog = []

with open("input.txt") as f:
    s1, s2  = f.read().split('\n\n')

    for s in s1.split('\n'):
        regs.append(int(s[12:]))

    prog = list(map(int, s2[9:].split(',')))

ADV = 0
BXL = 1
BST = 2
JNZ = 3
BXC = 4
OUT = 5
BDV = 6
CDV = 7

def run(regs, prog):
    ra = regs[0]
    rb = regs[1]
    rc = regs[2]

    def get_combo(n):
        if 0 <= n <= 3:
            return n
        if n == 4:
            return ra
        if n == 5:
            return rb
        if n == 6:
            return rc

    out = []

    ip = 0
    while ip < len(prog):
        opcode = prog[ip]
        operand = prog[ip+1]
        if opcode == ADV:
            ra = ra >> get_combo(operand)
        elif opcode == BXL:
            rb = rb ^ operand
        elif opcode == BST:
            rb = get_combo(operand) & 7
        elif opcode == JNZ:
            if ra != 0:
                ip = operand - 2
        elif opcode == BXC:
            rb = rb ^ rc
        elif opcode == OUT:
            out.append(get_combo(operand) & 7)
        elif opcode == BDV:
            rb = ra >> get_combo(operand)
        elif opcode == CDV:
            rc = ra >> get_combo(operand)

        ip += 2

    return out


def part1():
    print(",".join(map(str, run(regs, prog))))


def part2():
    def search(prog, a, pos):
        for k in range(8):
            z = k << (3 * pos)
            if a + z == 0:
                continue
            out = run((a + z, 0, 0), prog)
            if out[pos] == prog[pos]:
                if pos == 0:
                    return z
                lower = search(prog, a + z, pos-1)
                if lower is not None:
                    return z + lower
        return None


    ra = search(prog, 0, len(prog) - 1)
    print(ra)


part1()
part2()
