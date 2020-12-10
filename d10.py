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

lms = len(ms)
print(ms)
mt = 0
def perms(i):#, ll):
    if i == lms - 1:
        return 1
    # print("push", i)
    t = 0
    for j in range(i + 1, i + 4):
        if j < lms and ms[j] <= ms[i] + 3:
            t += perms(j)
            # t += perms(j, ll[:] + [ms[j]])

        else:
            break
    # print("pop", i, t, ll)
    global mt
    if t > mt:
        print(mt)
        mt = t
    return t

print("2:", perms(0))
# print(perms(0, [ms[0]]))
