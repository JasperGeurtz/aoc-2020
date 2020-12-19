import utils

m = utils.opener.raw("input/19.txt")
mm = m.split("\n\n")

def get_rules(rows):
    rules = {}
    for r in rows:
        k, v = r.split(": ")
        v = v.split("|")
        v = [[int(q) if q.isnumeric() else q.replace('"', '') for q in x.strip().split(" ")] for x in v]
        rules[int(k)] = v
    return rules

def check(rules, msg, key=0):
    possible = []
    for anyrules in rules[key]:  # these are OR
        some = []
        if type(anyrules[0]) == str:
            if msg:
                some.append((msg[0] == anyrules[0], msg[1:]))
        else:
            some = [(True, msg)]
            for allrules in anyrules:  # these are AND
                newsome = []
                for flg, msg3 in some[:]:
                    if flg and msg3:
                        poss_msgs = check(rules, msg3[:], allrules)
                        newsome += poss_msgs
                some = newsome
        if some:
            possible += some
    return possible


s1 = 0
rules1 = get_rules(mm[0].split("\n"))
messages = mm[1].split("\n")[:-1]

for msg in messages:
    results = check(rules1, msg)
    s1 += 1 if any([valid and not left for valid, left in results]) else 0
print("1: ", s1)

m2 = m.replace("8: 42", "8: 42 | 42 8").replace("11: 42 31", "11: 42 31 | 42 11 31")
rules2 = get_rules(m2.split("\n\n")[0].split("\n"))
s2 = 0
for msg in messages:
    results = check(rules2, msg)
    s2 += 1 if any([valid and not left for valid, left in results]) else 0
print("2: ", s2)

