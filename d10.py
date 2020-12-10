import utils

m = utils.opener.numbers("input/10.txt")

ms = [0] + sorted(m) + [max(m) + 3]
diffs = {}
for i in range(1, len(ms)):
    c = ms[i] - ms[i - 1]
    if c not in diffs:
        diffs[c] = 0
    diffs[c] += 1

print("1:", diffs[1] * diffs[3])


cache = {}

def perms(i):
    if i in cache:
        return cache[i]
    if i == len(ms) - 1:
        return 1
    t = 0
    for j in range(i + 1, i + 4):
        if j < len(ms) and ms[j] <= ms[i] + 3:
            t += perms(j)
        else:
            break
    cache[i] = t
    return t

print("2:", perms(0))
