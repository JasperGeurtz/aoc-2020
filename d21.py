import utils

m = utils.opener.lines("input/21.1.txt")


"""
Each allergen is found in exactly one ingredient.
Each ingredient contains zero or one allergen.
Allergens aren't always marked; 
"""
foods = []
appearances = {}
allergens = {}

for line in m:
    ingredients, contains = line.split(" (contains ")
    ingredients = set(ingredients.split(" "))
    contains = set(contains[:-1].split(", "))


    print("line", ingredients, contains)

    for ing in ingredients:
        if ing not in allergens:
            allergens[ing] = {}
            appearances[ing] = 0
        appearances[ing] += 1

    foods.append((ingredients, contains))


print("foods:", foods)
print("appearances:", appearances)
print("allergens:", allergens)
print("mxmxvkd, kfcds, sqjhc, nhms")


"""
mxmxvkd kfcds sqjhc nhms (contains dairy, fish)
trh fvjkl sbzzf mxmxvkd (contains dairy)
sqjhc fvjkl (contains soy)
sqjhc mxmxvkd sbzzf (contains fish)

step 1: mxmxvkd kfcds sqjhc nhms (contains dairy, fish)
mxmxvkd = dairy, fish
kfcds = dairy, fish
sqjhc = dairy, fish
nhms = dairy, fish

step 2: trh fvjkl sbzzf mxmxvkd (contains dairy)
mxmxvkd = dairy !(fish removed)
kfcds = fish
sqjhc = fish
nhms = fish
trh = 
fvjkl = 
sbzzf = 

step 3: sqjhc fvjkl (contains soy)
mxmxvkd = dairy
kfcds = fish
sqjhc = fish, soy
nhms = fish
trh = 
fvjkl = soy
sbzzf = 

step 4: sqjhc mxmxvkd sbzzf (contains fish)
mxmxvkd = dairy
kfcds = 
sqjhc = fish
nhms = 
trh = 
fvjkl = soy
sbzzf = 
kfcds, nhms, sbzzf, or trh
"""