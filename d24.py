import utils

m = utils.opener.lines("input/24.txt")

"""
six neighbors: east, southeast, southwest, west, northwest, and northeast. 
These directions are given in your list, respectively, as e, se, sw, w, nw, and ne
   
        (-1,0/-1)   (-1,1/0)
           NW    NE

(0, -1) W    (0,0)   E (0,1)

            SW    SE 
        (1, 0/-1)      (1, 1/0)
"""

dirs = {
    "e": [(0, 1), (0, 1)], # depends on odd or even row in 2D grid
    "se": [(1, 1), (1, 0)],
    "sw": [(1, 0), (1, -1)],
    "w": [(0, -1), (0, -1)],
    "nw": [(-1, 0), (-1, -1)],
    "ne": [(-1, 1), (-1, 0)],
}

black = set()
center = (0, 0)
for line in m:
    curr = center
    while line:
        i = 2 if line[:2] in dirs else 1
        mv, line = line[:i], line[i:]
        tk = dirs[mv][0 if curr[0] % 2 else 1] # odd or even row
        curr = (curr[0] + tk[0], curr[1] + tk[1])

    if curr in black:
        black.remove(curr) # becomes white
    else:
        black.add(curr)

print("1:", len(black))


def neighbours(n):
    return [(n[0] + d[0], n[1] + d[1]) for d in [dirs[v][0 if n[0] % 2 else 1] for v in dirs]]


for _ in range(100):
    to_remove = []
    to_add = []
    white = set()
    for bn in black:
        bc = 0
        for n in neighbours(bn):
            if n in black:
                bc += 1
            else:
                white.add(n)
        if bc == 0 or bc > 2:
            to_remove.append(bn)

    for wn in white:
        bc = 0
        for n in neighbours(wn):
            if n in black:
                bc += 1
        if bc == 2:
            to_add.append(wn)

    for n in to_remove:
        black.remove(n)
    for n in to_add:
        black.add(n)

print("2:", len(black))