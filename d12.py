import utils

m = utils.opener.lines("input/12.txt")

loc = [0, 0]
rots = [[0, -1], [1, 0], [0, 1], [-1, 0]]
ri = 1
for ins in m:
    a, b = ins[0], int(ins[1:])

    if a == "N":
        loc[1] -= b
    elif a == "S":
        loc[1] += b
    elif a == "E":
        loc[0] += b
    elif a == "W":
        loc[0] -= b

    elif a == "L":
        ri = (ri - b // 90) % len(rots)
    elif a == "R":
        ri = (ri + b // 90) % len(rots)
    elif a == "F":
        loc[0] += b * rots[ri][0]
        loc[1] += b * rots[ri][1]

s1 = abs(loc[0]) + abs(loc[1])
print("1: ", s1)

loc = [0, 0]
way = [10, -1]
for ins in m:
    a, b = ins[0], int(ins[1:])

    if a == "N":
        way[1] -= b
    elif a == "S":
        way[1] += b
    elif a == "E":
        way[0] += b
    elif a == "W":
        way[0] -= b

    elif a == "L":
        for _ in range(b // 90):
            w = way[:]
            way[0] = 1 * w[1]
            way[1] = -1 * w[0]
    elif a == "R":
        for _ in range(b // 90):
            w = way[:]
            way[0] = -1 * w[1]
            way[1] = 1 * w[0]
    elif a == "F":
        loc[0] += b * way[0]
        loc[1] += b * way[1]

s2 = abs(loc[0]) + abs(loc[1])
print("2: ", s2)
