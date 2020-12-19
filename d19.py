import utils

m = utils.opener.raw("input/19.2.txt")

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
    valid = False
    for subrules in rules[key]:  # these are OR
        if type(subrules[0]) == str:
            if not msg:
                return False, ""
            return msg[0] == subrules[0], msg[1:]
        else:
            vv = True
            msg2 = msg[:]
            for r in subrules:  # these are AND
                v, msg2 = check(rules, msg2[:], r)
                if not v:
                    vv = False
                    break

        if vv:
            valid = True
            msg = msg2[:]
            break
    return valid, msg[:]


s1 = 0
rules1 = get_rules(mm[0].split("\n"))
for msg in mm[1].split("\n")[:-1]:
    valid, left = check(rules1, msg)
    s1 += 1 if valid and not left else 0
print("1: ", s1)

def debug(level, *str):
    # return
    if level > 0:
        return
    print(level, level*"     ", *str)

def check2(rules, msg, key=0, level=0):
    debug(level, "start", key, msg, rules[key])
    valid = False
    for subrules in rules[key]:  # these are OR
        debug(level, " - subrules", subrules)
        vv = True
        msg2 = msg[:]
        if type(subrules[0]) == str:
            if msg:
                debug(level, "leaf:", msg[0], subrules[0], msg[1:])
                vv = msg[0] == subrules[0]
            else:
                vv = False
            msg2 = msg[1:]
        else:
            possible = []
            for r in subrules:  # these are AND
                v, msg2 = check2(rules, msg2, r, level+1)
                if not v:
                    debug(level, "   - false:", r, msg2)
                    vv = False
                    break
                else:
                    debug(level, "   - true:", r, msg2)

        if vv:
            valid = True
            msg = msg2[:]
            debug(level, " - valid", msg)
            break
    debug(level, "end", key, valid, msg)
    return valid, msg[:]


m2 = m.replace("8: 42", "8: 42 | 42 8").replace("11: 42 31", "11: 42 31 | 42 11 31")
mm2 = m2.split("\n\n")
rules2 = get_rules( mm2[0].split("\n"))
print(rules2)
s2 = 0

# test = "aaaabbaaaabbaaa"
# print(test, check2(rules2, test))

for msg in mm2[1].split("\n")[:-1]:
    valid, left = check2(rules2, msg)
    s2 += 1 if valid and not left else 0
    print("END", msg, valid, left)
print("2: ", s2)

