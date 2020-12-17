import utils

m = utils.opener.grid("input/17.txt")

cubes = set()
for x in range(len(m[0])):
    for y in range(len(m)):
        if m[x][y] == "#":
            cubes.add((x, y, 0))

def neighbours(c):
    res = set()
    for i in [-1, 0, 1]:
        for j in [-1, 0, 1]:
            for k in [-1, 0, 1]:
                if (i,j,k) != (0,0,0):
                    res.add((c[0] + i, c[1] + j, c[2] + k))
    return res


for cycle in range(6):
    newcubes = set()
    potential = {}
    for c in cubes:
        ns = neighbours(c)
        valid_ns = len(ns.intersection(cubes))
        if valid_ns in [2, 3]: # stay ACTIVE:
            newcubes.add(c)

        future_ns = ns.difference(cubes)
        for dn in future_ns:
            potential[dn] = 1 + (potential[dn] if dn in potential else 0)
        # print(c, valid_ns, ns)

    for pc, pv in potential.items():
        if pv == 3: # become ACTIVE
            newcubes.add(pc)
    cubes = newcubes

print("1:", len(cubes))




cubes = set()
for x in range(len(m[0])):
    for y in range(len(m)):
        if m[x][y] == "#":
            cubes.add((x, y, 0, 0))

def neighbours(c):
    res = set()
    for i in [-1, 0, 1]:
        for j in [-1, 0, 1]:
            for k in [-1, 0, 1]:
                for l in [-1, 0, 1]:
                    if (i,j,k, l) != (0,0,0,0):
                        res.add((c[0] + i, c[1] + j, c[2] + k, c[3] + l))
    return res


for cycle in range(6):
    newcubes = set()
    potential = {}
    for c in cubes:
        ns = neighbours(c)
        valid_ns = len(ns.intersection(cubes))
        if valid_ns in [2, 3]: # stay ACTIVE:
            newcubes.add(c)
        future_ns = ns.difference(cubes)
        for dn in future_ns:
            potential[dn] = 1 + (potential[dn] if dn in potential else 0)

    for pc, pv in potential.items():
        if pv == 3: # become ACTIVE
            newcubes.add(pc)
    cubes = newcubes

print("2:", len(cubes))
