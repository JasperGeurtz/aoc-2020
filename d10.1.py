import utils

m = utils.opener.numbers("input/10.txt")

ms = [0] + sorted(m) + [max(m) + 3]

ns = [int(x) for x in """0
1
2
4
7
14
28
49
98
196
392
784
1372
2744
5488
9604
19208
38416
67228
134456
268912
537824
1075648
1882384
3764768
7529536
15059072
30118144
60236288
120472576
210827008""".split("\n")]

for i in range(1, len(ns)):
    # print(i, ms[i], ns[i], ns[i-1], ns[i]*2, ns[i]*2 - ns[i-1])
    print(f"from {ms[i-1]} to {ms[i]}: {ns[i]}")
    pass


lms = len(ms)
tot = 1
for i in range(0, lms-1):
    tot *= 2
    if ms[i+1] - ms[i] == 3:
        tot -= int(tot / 8)
    # print(i, ms[i+1], ms[i], tot, ns[i+1])
print("2:", tot)
# print(perms(0, [ms[0]]))
