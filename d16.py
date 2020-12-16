import utils

m = utils.opener.raw("input/16.txt")
rm, tm, om = m.split("\n\n")

rules = {}
for line in rm.split("\n"):
    name, expr = line.split(": ")
    rules[name] = [[int(q) for q in x.split("-")] for x in expr.split(" or ")]

myticket = [int(x) for x in tm.split("\n")[1].split(",")]
tickets = [[int(q) for q in x.split(",")] for x in tm.split("\n")[1:] + om.split("\n")[1:-1]]

s1 = 0
for t in tickets[:]:
    for v in t:
        if not any([r[0][0] <= v <= r[0][1] or r[1][0] <= v <= r[1][1] for r in rules.values()]):
            s1 += v
            tickets.remove(t)

print("1:", s1)

possible = {}
for rule in rules:
    possible[rule] = set(range(len(myticket)))

for t in tickets:
    for i, v in enumerate(t):
        for rname, r in rules.items():
            if not (r[0][0] <= v <= r[0][1] or r[1][0] <= v <= r[1][1]):
                if i in possible[rname]:
                    possible[rname].remove(i)

found = {}
while possible:
    k, v = min(possible.items(), key=lambda item: item[1])
    found[k] = list(v)[0]
    del possible[k]
    for val in possible.values():
        val.remove(found[k])

s2 = 1
for k, v in found.items():
    if k.startswith("departure"):
        s2 *= myticket[v]

print("2:", s2)
