import utils
m = "643719258"

initial_cups = [int(x) for x in list(m)]

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class CircularLinkedList:
    def __init__(self, values):
        self.root = Node(values[0])
        self.lookup = {values[0]: self.root}
        last = self.root
        for v in values[1:]:
            last.next = Node(v)
            last = last.next
            self.lookup[v] = last
        last.next = self.root

def play(cll, moves):
    curr = cll.root
    max_cups = max(cll.lookup.keys())
    for _ in range(moves):
        rem = [curr.next, curr.next.next, curr.next.next.next]
        goal_v = curr.value - 1
        while goal_v == 0 or goal_v in [r.value for r in rem]:
            goal_v = goal_v - 1 if goal_v > 0 else max_cups
        goal_node = cll.lookup[goal_v]
        curr.next = rem[2].next
        temp = goal_node.next
        goal_node.next = rem[0]
        rem[2].next = temp
        curr = curr.next
    return cll

res = play(CircularLinkedList(initial_cups), 100)
curr = res.lookup[1].next
s1 = []
while curr.value != 1:
    s1.append(str(curr.value))
    curr = curr.next
print("1:", "".join(s1))

res = play(CircularLinkedList(initial_cups + [x for x in range(10, 1_000_000 + 1)]), 10_000_000)
one = res.lookup[1]
s2 = one.next.value * one.next.next.value
print("2:", s2)
