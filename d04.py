import utils

m = utils.opener.raw("input/04.txt")[:-1]

rt = [(" ", ","), ("\n", ","), (":", "':'"), (",", "','")]
pp = [eval("{'" + utils.replaceAll(p, rt) + "'}") for p in m.split("\n\n")] # list of dicts representing passports

btwn = lambda a, f, b: a <= int(f) <= b

s1 = 0
s2 = 0
for p in pp:
    if (len(p) == 8) or (len(p) == 7 and "cid" not in p):
        s1 += 1

        byr, iyr, eyr, hgt, hcl, ecl, pid = p["byr"], p["iyr"], p["eyr"], p["hgt"], p["hcl"], p["ecl"], p["pid"]
        if (btwn(1920, byr, 2002) and btwn(2010, iyr, 2020) and btwn(2020, eyr, 2030)) and (
                (hgt.endswith("cm") and btwn(150, hgt[:-2], 193)) or (hgt.endswith("in") and btwn(59, hgt[:-2], 76))) and (
                len(hcl) == 7 and hcl[0] == "#" and all([x in utils.hexanums for x in hcl[1:]])) and (
                ecl in {"amb", "blu", "brn", "gry", "grn", "hzl", "oth"}) and (
                len(pid) == 9 and all([x in utils.nums for x in p["pid"]])):
            s2 += 1

print("1:", s1)
print("2:", s2)
