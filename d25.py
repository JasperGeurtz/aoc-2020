import utils

m = utils.opener.numbers("input/25.txt")
pubs = m[:]

mod = 20201227
k = 1
sub = 7
loop = 0

while pubs:
    k = (k * sub) % mod
    loop += 1
    if k in pubs:
        pubs.remove(k)
        break
k = 1
sub = pubs[0]
for _ in range(loop):
    k = (k * sub) % mod

print("1:", k)
