import utils

m = utils.opener.grid("input/17.txt")


def neighbours(dims):
    def curried(c):
        ns = set([tuple(x) for x in neighbours_list(c, dims)])
        ns.remove(c)
        return ns

    return curried


def neighbours_list(c, dims):
    if dims == 1:
        return [[c[0] - 1], [c[0]], [c[0] + 1]]
    res = []
    for t in neighbours_list(c, dims - 1):
        for x in [-1, 0, 1]:
            res.append(t[:] + [c[dims - 1] + x])
    return res


def simulate(grid, dims, cycles=6):
    neighbours_func = neighbours(dims)
    cubes = set([tuple([x, y] + ((dims - 2) * [0])) for x in range(len(grid[0])) for y in range(len(grid)) if
                 grid[x][y] == "#"])
    for _ in range(cycles):
        potential = {}
        oldcubes = set(cubes)
        for c in oldcubes:
            ns = neighbours_func(c)
            if len(ns.intersection(oldcubes)) not in [2, 3]:
                cubes.remove(c)
            for dn in ns.difference(oldcubes):
                potential[dn] = 1 + (potential[dn] if dn in potential else 0)
        for pc, pv in potential.items():
            if pv == 3:
                cubes.add(pc)
    return cubes


print("1:", len(simulate(m, 3)))
print("2:", len(simulate(m, 4)))
