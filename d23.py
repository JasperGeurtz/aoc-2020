from tqdm import tqdm
m = "643719258"
# m = "389125467"

initial_cups = [int(x) for x in list(m)]

def play(cups, moves):
    idx = 0
    for _ in tqdm(range(moves)):
        curr = cups[idx]
        rem_i = [(idx + i) % len(cups) for i in range(1, 4)]
        rem = [cups[i] for i in rem_i]
        for p in rem:
            cups.remove(p)

        goal = curr - 1
        while goal not in cups:
            goal -= 1
            if goal <= 0:
                goal = max(cups)
        goal_i = cups.index(goal) + 1
        cups = cups[:goal_i] + rem + cups[goal_i:]
        idx = (cups.index(curr) + 1) % len(cups)
    return cups

end = play(initial_cups[:], 100)
one = end.index(1)
s1 = "".join(str(end[(one + i) % len(end)]) for i in range(1, len(end)))

print("1:", s1)

cups2 = initial_cups[:] + [x for x in range(10, 1_000_001)]

end = play(cups2, 10_000_000)
one = end.index(1)

s2 = end[(one + 1) % len(cups2)] * end[(one + 2) % len(cups2)]
print(s2)
