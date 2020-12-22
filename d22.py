import utils

m = utils.opener.lines("input/22.txt")

players = []
for line in m:
    if not line:
        continue
    if line.startswith("Player"):
        players.append([])
    else:
        players[-1].append(int(line))


def combat(p0, p1):
    while p0 and p1:
        c0 = p0.pop(0)
        c1 = p1.pop(0)
        if c0 > c1:
            p0.append(c0)
            p0.append(c1)
        else:
            p1.append(c1)
            p1.append(c0)
    score = 0
    winner = p0 if p0 else p1
    for i, e in enumerate(reversed(winner)):
        score += (i + 1) * e
    return score

s1 = combat(*[x[:] for x in players])
print("1:", s1)

def recur_combat(p0, p1, game=0):
    seen = set()

    while p0 and p1:

        c0 = p0.pop(0)
        c1 = p1.pop(0)
        if len(p0) >= c0 and len(p1) >= c1:

            wnr = recur_combat(p0[:c0], p1[:c1], game + 1)
        else:
            wnr = 0 if c0 > c1 else 1
        if wnr == 0:
            p0.append(c0)
            p0.append(c1)
        else:
            p1.append(c1)
            p1.append(c0)

        config = tuple((tuple(p0), tuple(p1)))
        if config in seen: # Rule 1
            return 0
        else:
            seen.add(config)

    winner = p0 if p0 else p1

    if game == 0:
        score = 0
        for i, e in enumerate(reversed(winner)):
            score += (i + 1) * e
        return score
    else:
        return 0 if winner == p0 else 1

s2 = recur_combat(*[x[:] for x in players])
print("2:", s2)
