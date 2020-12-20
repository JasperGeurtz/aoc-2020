import utils

m = utils.opener.raw("input/20.txt")[:-1]

images = {}
for img in m.split("\n\n"):
    id = int(img.split("\n")[0].split(" ")[1][:-1])
    rows = [tuple(x) for x in img.split("\n")[1:]]

    images[id] = rows

print(len(images))


def display(img):
    print("\n".join(["".join(x) for x in img]))


def copy(img):
    return [x[:] for x in img]


def rotate(img):
    return list(zip(*img[::-1]))


def flip(img, dim):
    if dim == 0:
        return img[::-1]
    if dim == 1:
        return [x[::-1] for x in img]

#
# arr = list(images.values())[0]
# display(arr)
# print("""""""")
#
# print(arr == rotate(rotate(rotate(rotate(arr)))))
# display(flip(arr, 0))
# print("""""""")
# print("""""""")
# display(flip(arr, 1))

def check_borders(image, jimage):
    border_dirs = []
    n = len(image)
    # tuple = (x, y, r, f)
    prev = []
    for rot in range(4):
        rot_jimage = copy(jimage)
        jimage = copy(jimage)
        for fdim in range(3):
            if jimage in prev:
                continue
            prev.append(copy(jimage))
            if all([image[0][i] == jimage[n - 1][i] for i in range(n)]):
                border_dirs.append((0, -1, rot, fdim))
            if all([image[n - 1][i] == jimage[0][i] for i in range(n)]):
                border_dirs.append((0, 1, rot, fdim))
            if all([image[i][0] == jimage[i][n - 1] for i in range(n)]):
                border_dirs.append((-1, 0, rot, fdim))
            if all([image[i][n - 1] == jimage[i][0] for i in range(n)]):
                border_dirs.append((0, -1, rot, fdim))
            jimage = flip(copy(jimage), fdim)

        jimage = rotate(copy(rot_jimage))


    return border_dirs


ids = list(images.keys())
neighbours = {}
for id in ids:
    image = images[id]
    print(id)
    # display(image)
    neighbours[id] = []
    for jid in ids:
        if id == jid:
            continue
        jimage = images[jid]
        border_dirs = check_borders(copy(image), copy(jimage))
        if border_dirs:
            neighbours[id].append((jid, border_dirs))
        # print(id, jid, border_dirs)

print("\n".join([str(x) for x in sorted(neighbours.items(), key=lambda k: -len(k[1]))]))


corners = [k for k, v in neighbours.items() if len(v) == 2]
print(corners)
print(len(corners))
s1 = utils.multiply(corners)
print("1:", s1)
