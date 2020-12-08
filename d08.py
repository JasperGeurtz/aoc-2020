import utils

m = utils.opener.lines("input/08.txt")

instructions = [[i.split(" ")[0], int(i.split(" ")[1])] for i in m]


def interpreter(instr):
    acc = 0
    index = 0
    seen = set()
    while index < len(instr):
        op, val = instr[index]
        if index in seen:
            return False, acc
        else:
            seen.add(index)

        if op == "acc":
            acc += val
            index += 1
        elif op == "jmp":
            index += val
        elif op == "nop":
            index += 1
        else:
            print(f"UNKNOWN OPCODE: {op} {val}")
    return True, acc


s1 = interpreter(instructions)[1]
print("1:", s1)

s2 = 0
for i, ix in enumerate(instructions):
    patched = [[u, v] for u, v in instructions]
    res = False
    if ix[0] == "nop":
        patched[i][0] = "jmp"
        res, s2 = interpreter(patched)
    elif ix[0] == "jmp":
        patched[i][0] = "nop"
        res, s2 = interpreter(patched)
    if res:
        break

print("2", s2)
