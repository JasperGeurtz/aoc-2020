import utils

m = utils.opener.raw("input/20.txt")
m = utils.opener.raw("input/20.1.txt")

tiles = {}

# KLEINE ITERMEZZO, MOET AVONDETEN PREPPEN

class Tile:
    def __init__(self, top, right, bottom, left):
        self.top = top
        self.right = right
        self.bottom = bottom
        self.left = left
        #zip(*original[::-1])
        #flip it, ship it, add get_inside functie

    def __repr__(self):
        square = f"\n{' ' .join(list(self.top))}"
        for i in range(1, len(top) - 1):
            square += f"\n{self.left[i]}{' ' * (2*len(top) - 3)}{self.right[i]}"
        square += f"\n{' ' .join(list(self.bottom))}\n"
        return square

    def rotate(self):  # right by 90
        top, right, bottom, left = self.left[::-1], self.top, self.right[::-1], self.bottom
        return Tile(top, right, bottom, left)

    def flip(self):
        top, bottom = self.bottom, self.top
        right, left = self.right[::-1], self.left[::-1]
        return Tile(top, right, bottom, left)

    def common_border(self, other):
        return self.left == other.right or self.right == other.left \
               or self.top == other.bottom or self.bottom == other.top

    def __eq__(self, other):
        return self.top == other.top and self.right == other.right \
               and self.bottom == other.bottom and self.left == other.left


for img in m[:-1].split("\n\n"):
    id = int(img.split("\n")[0].split(" ")[1][:-1])
    content = img.split("\n")[1:]
    top, bottom = content[0][:], content[-1][:]
    left, right = "".join([r[0] for r in content]), "".join([r[-1] for r in content])
    tile = Tile(top, right, bottom, left)
    tiles[id] = tile

# print("\n".join(str(x) for x in tiles.items()))

matches = {}

for id, tile in tiles.items():
    matches[id] = []
    for p_id, p_tile in tiles.items():
        if p_id == id:
            continue
        for i in range(4):
            if tile.common_border(p_tile):
                matches[id].append(p_id)
                break

            f_tile = p_tile.flip()
            if tile.common_border(f_tile):
                matches[id].append(p_id)
                break

            p_tile = p_tile.rotate()

print(matches)
edges = [k for k, v in matches.items() if len(v) == 2]
print("1: ", utils.multiply(edges))

### build the image

# center =