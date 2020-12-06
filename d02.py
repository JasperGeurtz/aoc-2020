import utils

lines = [x.split(": ") for x in utils.opener.lines("input/02.txt")]

a = 0
b = 0
for nmc, s in lines:
    nm, c = nmc.split(" ")
    n, m = [int(x) for x in nm.split("-")]

    if n <= len(s.split(c)) - 1 <= m:
        a += 1
    if (s[n-1] == c) ^ (s[m-1] == c):
        b += 1
print("1:", a)
print("2:", b)
