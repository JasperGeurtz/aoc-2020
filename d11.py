import utils
import time
m = utils.opener.grid("input/11.txt")


start = time.time()

height = len(m)
width = len(m[0])

dirs = [(-1, -1), (0, -1), (1, -1),
        (-1, 0),           (1, 0),
        (-1, 1),  (0, 1),  (1, 1)]

changed = True
old = [x[:] for x in m[:]]
while changed:
    new = [x[:] for x in old[:]]
    changed = False
    for y in range(height):
        for x in range(width):
            c = old[y][x]
            occ = 0
            for i, j in dirs:
                i += y
                j += x
                if 0 <= i < height and 0 <= j < width:
                    if old[i][j] == "#":
                        occ += 1
            if c == 'L' and not occ:
                new[y][x] = "#"
                changed = True
            elif c == '#' and occ >= 4:
                new[y][x] = "L"
                changed = True
    old = new


s1 = 0
for col in old:
    for el in col:
        if el == "#":
            s1 += 1
print("1:", s1, time.time() - start)

start = time.time()
changed = True
old = [x[:] for x in m[:]]
while changed:
    new = [x[:] for x in old[:]]
    changed = False
    for y in range(height):
        for x in range(width):
            c = old[y][x]
            occ = 0
            for i, j in dirs:
                t = 0
                while True:
                    t += 1
                    a = y + t * i
                    b = x + t * j
                    if 0 <= a < height and 0 <= b < width:
                        if old[a][b] == "#":
                            occ += 1
                            break
                        if old[a][b] == "L":
                            break
                    else:
                        break
            if c == 'L' and not occ:
                new[y][x] = "#"
                changed = True
            elif c == '#' and occ >= 5:
                new[y][x] = "L"
                changed = True
    old = new


s2 = 0
for col in old:
    for el in col:
        if el == "#":
            s2 += 1
print("2:", s2, time.time() - start)


