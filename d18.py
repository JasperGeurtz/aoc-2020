import utils

m = utils.opener.lines("input/18.txt")


def find_matching(expr, i, dir):
    other = ")" if dir == "(" else "("
    rge = [i+1, len(expr)] if dir == "(" else [i-1, -1, -1]
    ctr = 1
    for j in range(*rge):
        if expr[j] == dir:
            ctr += 1
        elif expr[j] == other:
            ctr -= 1
            if ctr == 0:
                return j
    raise ("error: ", expr, i, expr[i])

def calc1(expr):
    t = 0
    i = 0
    while i < len(expr):
        c = expr[i]
        if c in "+*":
            if expr[i + 1] == "(":
                mi = find_matching(expr, i + 1, "(")
                s = calc1(expr[i + 2:mi])
                i = mi
            else:
                s = int(expr[i + 1])
                i += 1
            if c == "+":
                t += s
            if c == "*":
                t *= s
        elif c == "(":
            mi = find_matching(expr, i, "(")
            t += calc1(expr[i + 1:mi])
            i = mi
        else:
            t = int(c)
        i += 1
    return t


s1 = sum([calc1(list(line.replace(" ", ""))) for line in m])
print("1: ", s1)


def calc2(expr):
    i = 0
    while i < len(expr):
        c = expr[i]
        if c == "+":
            mil = find_matching(expr, i-1, ")") + 1 if expr[i-1] == ")" else i-1
            mir = find_matching(expr, i + 1, "(") + 1 if expr[i+1] == "(" else  i+2
            expr = expr[:mil] + ["("] + expr[mil:mir] + [")"] + expr[mir:]
            i += 1
        i += 1
    return calc1(expr)

s2 = sum([calc2(list(line.replace(" ", ""))) for line in m])
print("2: ", s2)
