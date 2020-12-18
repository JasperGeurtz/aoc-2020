import utils

m = utils.opener.lines("input/18.txt")


def find_matching_right(expr, i, ):
    ctr = 1
    for j in range(i + 1, len(expr)):
        if expr[j] == "(":
            ctr += 1
        elif expr[j] == ")":
            ctr -= 1
            if ctr == 0:
                return j
    raise ("error: ", expr, i, expr[i])


def calc1(expr):
    t = 0
    i = 0
    while i < len(expr):
        c = expr[i]
        if c == "+":
            if expr[i + 1] == "(":
                mi = find_matching_right(expr, i + 1)
                s = calc1(expr[i + 2:mi])
                i = mi
            else:
                s = int(expr[i + 1])
                i += 1
            t += s
        elif expr[i] == "*":
            if expr[i + 1] == "(":
                mi = find_matching_right(expr, i + 1)
                s = calc1(expr[i + 2:mi])
                i = mi
            else:
                s = int(expr[i + 1])
                i += 1
            t *= s
        elif c == "(":
            mi = find_matching_right(expr, i)
            t += calc1(expr[i + 1:mi])
            i = mi
        else:
            t = int(c)
        i += 1
    return t


s1 = 0
for line in m:
    s1 += calc1(list(line.replace(" ", "")))
print("1: ", s1)

def find_matching_left(expr, i):
    ctr = 1
    for j in range(i-1, -1, -1):
        if expr[j] == ")":
            ctr += 1
        elif expr[j] == "(":
            ctr -= 1
            if ctr == 0:
                return j
    raise ("error: ", expr, i, expr[i])



def calc2(expr):
    i = 0
    while i < len(expr):
        c = expr[i]
        if c == "+":
            if expr[i-1] == ")":
                mil = find_matching_left(expr, i-1) + 1
            else:
                mil = i-1
            if expr[i+1] == "(":
                mir = find_matching_right(expr, i + 1) + 1
            else:
                mir = i+2
            expr = expr[:mil] + ["("] + expr[mil:mir] + [")"] + expr[mir:]
            i += 1
        i += 1
    return calc1(expr)

s2 = 0
for line in m:
    s2 += calc2(list(line.replace(" ", "")))
print("2: ", s2)
