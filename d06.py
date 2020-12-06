import utils


m = utils.opener.raw("input/06.txt")[:-1].split("\n\n")

s1 = 0
s2 = 0
for group in m:
    yes = set(group.replace("\n", ""))
    s1 += len(yes)

    a = set(group.split("\n")[0])
    for line in group.split("\n")[1:]:
        for c in list(a):
            if c not in line:
                a.remove(c)

    s2 += len(a)

print("1:", s1)
print("2:", s2)
