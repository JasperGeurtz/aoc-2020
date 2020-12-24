import utils
import math

m = utils.opener.raw("input/20.txt")

class Tile:
    def __init__(self, content):
        self.content = content

    def __repr__(self):
        return "\n".join(self.content)

    def rotate(self):  # right by 90
        content = ["".join(x) for x in zip(*self.content[::-1])]
        return Tile(content)

    def flip(self):
        content = self.content[::-1]
        return Tile(content)

    def left(self):
        return "".join([r[0] for r in self.content])

    def right(self):
        return "".join([r[-1] for r in self.content])

    def top(self):
        return self.content[0][:]

    def bottom(self):
        return self.content[-1][:]

    def common_border(self, other):
        if self.left() == other.right():
            return 0, -1
        if self.right() == other.left():
            return 0, 1
        if self.top() == other.bottom():
            return -1, 0
        if self.bottom() == other.top():
            return 1, 0
        return False

    def peel(self):
        return [x[1:-1] for x in self.content[1:-1]]

tiles = {}
for img in m[:-1].split("\n\n"):
    id = int(img.split("\n")[0].split(" ")[1][:-1])
    tiles[id] = Tile(img.split("\n")[1:])

### FIND RELATIVE POSITIONS (ROTATED & FLIPPED WITH REPSECT TO "FIRST" TILE)
ordered = list(tiles.keys())
todo = [ordered[0]]
others = set(ordered[1:])
matches = {id: [] for id in ordered}

while todo:
    id = todo.pop(0)
    tile = tiles[id]
    for p_id in list(others):
        p_tile = tiles[p_id]
        for _ in range(4):
            total_tile = p_tile
            found = False
            for _ in range(2):
                border = tile.common_border(total_tile)
                if border:
                    matches[id].append([p_id, border])
                    tiles[p_id] = total_tile
                    todo.append(p_id)
                    others.remove(p_id)
                    found = True
                    break
                total_tile = total_tile.flip()
            if found:
                break
            p_tile = p_tile.rotate()

### BUILD THE GRID
first = max(matches.items(), key=lambda k: len(k[1]))[0]
grid_dict = {(0, 0) : first}
lookup = {first: (0, 0)} # inverse lookup table
todo = [first]
while todo:
    id = todo.pop(0)
    pos = lookup[id]
    for c_id, c_rel in matches[id]:
        todo.append(c_id)
        c_pos = (pos[0] + c_rel[0], pos[1] + c_rel[1])
        grid_dict[c_pos] = c_id
        lookup[c_id] = c_pos

size = int(math.sqrt(len(matches)))
grid = [size * [0] for _ in range(size)]
w_off = min([e[0] for e in grid_dict])
h_off = min([e[1] for e in grid_dict])

for g_pos, g_id in grid_dict.items():
    x, y = g_pos[0] - w_off, g_pos[1] - h_off
    grid[x][y] = g_id


corners = [grid[0][0], grid[0][size-1], grid[size-1][0], grid[size-1][size-1]]
print("1:", utils.multiply(corners))

### BUILD THE IMAGE
p_size = len(tiles[first].content) - 2
image = []

for x in range(size):
    image += [list() for _ in range(p_size)]
    for y in range(size):
        p = tiles[grid[x][y]].peel()
        for i, row in enumerate(p):
            image[i - p_size] += p[i]

### SEARCH THE MONSTER
monster = """
                  # 
#    ##    ##    ###
 #  #  #  #  #  #   
"""
monster = monster[1:-1].split("\n")
m_set = set()
m_h = len(monster)
m_w = len(monster[0])
for i in range(m_h):
    for j in range(m_w):
        if monster[i][j] == "#":
            m_set.add((i,j))

image_size = len(image)
t_image = Tile(image)
m_count = 0
for _ in range(4):
    total_tile = t_image
    found = False
    for _ in range(2):
        m_count = 0
        for i in range(0, image_size - m_h):
            for j in range(0, image_size - m_w):
                valid = all([t_image.content[i + h][j + w] == "#" for h, w in m_set])
                m_count += 1 if valid else 0
        if m_count:
            found = True
            break
        total_tile = total_tile.flip()
    if found:
        break
    t_image = t_image.rotate()

n_hashtags = sum([len([x for x in row if x == "#"]) for row in image])
n_mdiff = m_count * len(m_set)
print("2:", n_hashtags - n_mdiff)
