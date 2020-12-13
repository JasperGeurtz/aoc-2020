import utils

m = utils.opener.lines("input/13.txt")

start = int(m[0])
buses = [int(x) if x != "x" else "x" for x in m[1].split(",")]

best = float("infinity")
busn = -1
for n in buses:
    if n == "x":
        continue
    q = start // n
    if start % n:
        q += 1
    diff = q * n - start
    if diff < best:
        best = diff
        busn = n

s1 = best * busn
print("1:", s1)


buses = [(int(b), i) for i, b in enumerate(m[1].split(",")) if b != "x"]

todo = buses[1:]
index = 0
incr = 1
s2 = 0

while True:
    target = index * buses[0][0] - buses[0][1]
    for number, offset in todo[:]:
        if (target + offset) % number:
            break
        else: # found something to speed up brute-force
            incr *= number
            todo.remove((number, offset))
    else:
        s2 = target
        break
    index += incr

print("2:", s2)


