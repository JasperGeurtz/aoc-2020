import utils

m = utils.opener.lines("input/05.txt")

res = []
for t in m:
    ymin, ymax, xmin, xmax = 0, 127, 0, 7
    for c in t:
        if c == "F":
            ymax = ymin + (ymax - ymin) // 2
        elif c == "B":
            ymin = ymin + (ymax - ymin) // 2 + 1
        elif c == "L":
            xmax = xmin + (xmax - xmin) // 2
        elif c == "R":
            xmin = xmin + (xmax - xmin) // 2 + 1
    res.append(ymin * 8 + xmin)

print("1:", max(res))

s = sorted(res)
for i in range(1, len(s)):
    if s[i-1] + 1 != s[i]:
        print("2:", (s[i-1] + s[i]) // 2)
        break

