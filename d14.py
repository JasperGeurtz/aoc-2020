import utils

m = utils.opener.lines("input/14.txt")

memory = {}
mask = ""
mem = {}
for p in m:
    if p[:4] == "mask":
        mask = p[7:]
    elif p[:3] == "mem":
        exec(p)
        k, v = list(mem.items())[0]
        k, v = int(k), str(bin(int(v)))[2:][::-1]
        del mem[k]

        mm = list(mask)[::-1]
        for i in range(len(mm)):
            if mm[i] == "X":
                mm[i] = v[i] if i < len(v) else '0'

        endvalue = int(''.join(mm[::-1]), 2)  # base 2
        memory[k] = endvalue

s1 = sum(memory.values())

print("1:", s1)

memory = {}
mask = ""
mem = {}


def possibilities(number, inputs, res):
    if len(inputs) == 0:
        res.append(number)
    else:
        tl = number[:]
        tl[inputs[0]] = "0"
        possibilities(tl, inputs[1:], res)
        tr = number[:]
        tr[inputs[0]] = "1"
        possibilities(tr, inputs[1:], res)


for p in m:
    if p[:4] == "mask":
        mask = p[7:]
    elif p[:3] == "mem":
        exec(p)
        k, v = list(mem.items())[0]
        del mem[k]
        k, v = str(bin(int(k)))[2:][::-1], int(v)

        mm = list(mask)[::-1]
        xs = []
        for i in range(len(mm)):
            if mm[i] == "0":
                mm[i] = k[i] if i < len(k) else "0"
            if mm[i] == "X":
                xs.append(i)

        res = []
        possibilities(mm, xs, res)
        for poss in res:
            endkey = int(''.join(poss[::-1]), 2)  # base 2
            memory[endkey] = v

s2 = sum(memory.values())

print("2:", s2)
