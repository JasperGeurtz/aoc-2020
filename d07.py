import utils

m = utils.opener.lines("input/07.txt")

bags = {}
for line in m:
    a, b = line[:-1].split(" contain ")
    a = a.replace("bags", "").strip()
    b = b.replace("bags", "").replace("bag", "").split(", ")
    bags[a] = {}
    if b[0] == 'no other ':
        continue
    for e in b:
        k, v = e.split(" ")[0], " ".join(e.split(" ")[1:]).strip()
        bags[a][v] = int(k)

start = "shiny gold"

valid = {start}
potential = [start]
while potential:
    c = bags[potential.pop(0)]
    for bn, bb in bags.items():
        if bn in valid:
            continue
        if any([x in valid for x in bb.keys()]):
            potential.append(bn)
            valid.add(bn)

s1 = len(valid) - 1


def find_children(name):
    t = 1
    c = bags[name]
    for k, v in c.items():
        t += v * find_children(k)
    return t


s2 = find_children(start) - 1

print("s1", s1)
print("s2", s2)
