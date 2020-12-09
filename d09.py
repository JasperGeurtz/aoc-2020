import utils
import time
m = utils.opener.numbers("input/09.txt")

start_time = time.time()

curr = m[:25]
s1 = 0
for n in m[25:]:
    nset = set(curr)
    found = False
    for x in curr:
        if n - x in nset:
            found = True
            break
    curr.pop(0)
    curr.append(n)
    if not found:
        s1 = n
        break

print("1:", s1)

target = s1
pot = {}
s2 = 0
for i, n in enumerate(m):
    if s2 != 0:
        break
    for k in list(pot.keys()):
        pot[k].append(n)
        s = sum(pot[k])
        if s == target:
            s2 = min(pot[k]) + max(pot[k])
        elif s > target:
            del pot[k]
    pot[i] = [n]

print("2:", s2)
