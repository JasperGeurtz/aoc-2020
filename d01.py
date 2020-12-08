import utils

numbers = utils.opener.numbers("input/01.txt")

target = 2020

seen = set()
for n in numbers:
    if n in seen:
        print("1:", n * (target - n))
        break
    else:
        seen.add(target - n)

seen = dict()
for n in numbers:
    if (target - n) in seen:
        v = seen[target - n]
        if len(v) == 2:
            print("2:", n * v[0] * v[1])
            break
    else:
        for k in set(seen.keys()):
            if len(seen[k]) < 2 and k + n <= target:  # only for positive nums
                seen[k + n] = seen[k] + [n]
        seen[n] = [n]
