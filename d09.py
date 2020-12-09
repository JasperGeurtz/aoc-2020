import utils

m = utils.opener.numbers("input/09.txt")

curr = m[:25]
nset = set(curr)
s1 = 0
for n in m[25:]:
    for x in curr:
        if n - x in nset:
            break
    else:
        s1 = n
        break
    nset.remove(curr.pop(0))
    curr.append(n)
    nset.add(n)

print("1:", s1)

target = s1
pot = {}
s2 = 0
for i, n in enumerate(m):
    if s2 != 0:
        break
    for k in list(pot.keys()):
        pot[k][0] += n
        if pot[k][0] > target:
            del pot[k]
        else:
            pot[k][1].append(n)
            if pot[k][0] == target:
                s2 = min(pot[k][1]) + max(pot[k][1])
                break
    if n < target:
        pot[i] = [n, [n]]

print("2:", s2)