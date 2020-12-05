import utils

m = utils.opener.lines("input/03.txt")

x, y, t = 0, 0, 0
while y < len(m):
    if m[y][x] == "#":
        t += 1
    x = (x + 3) % len(m[0])
    y += 1

print("1:", t)

c = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
t = [0 for _ in range(len(c))]
for i, (xi, yi) in enumerate(c):
    x, y = 0, 0
    while y < len(m):
        if m[y][x] == "#":
            t[i] += 1
        x = (x + xi) % len(m[0])
        y += yi

print("2:", utils.multiply(t))
