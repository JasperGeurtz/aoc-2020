import utils

m = utils.opener.lines("input/21.txt")

appearances = {}
allergens = {}

for line in m:
    ingredients, contains = line.split(" (contains ")
    ingredients = set(ingredients.split(" "))
    contains = set(contains[:-1].split(", "))

    for ing in ingredients:
        if ing not in appearances:
            appearances[ing] = 0
        appearances[ing] += 1
    for c in contains:
        if c not in allergens:
            allergens[c] = []
        allergens[c].append(set(ingredients))

sure = {}
while allergens:
    for a in list(allergens.keys()):
        v = allergens[a]
        inter = v[0].intersection(*v[1:])
        if len(inter) == 1: # found only possibility
            found = list(inter)[0]
            sure[a] = found
            del allergens[a]
            for v in allergens.values():
                for ings in v:
                    if found in ings:
                        ings.remove(found)


s1 = sum([v for k, v in appearances.items() if k not in sure])
print("1:", s1)

s2 = ",".join([sure[k] for k in sorted(sure)])

print("2:", s2)
