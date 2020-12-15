import utils

m = [int(x) for x in utils.opener.lines("input/15.txt")[0].split(",")]


def play(target):
    occs = {}
    for i, n in enumerate(m):
        occs[n] = [i]

    last = m[-1]
    for i in range(len(m), target):
        n = 0

        if len(occs[last]) > 1:
            n = occs[last][-1] - occs[last][-2]

        last = n
        if n in occs:
            occs[n].append(i)
        else:
            occs[n] = [i]
    return last


s1 = play(2020)
print("1:", s1)

s2 = play(30000000)
print("2:", s2)
