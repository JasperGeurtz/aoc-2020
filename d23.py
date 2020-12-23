from tqdm import tqdm
import utils
m = "643719258"
# m = "389125467"

initial_cups = [int(x) for x in list(m)]

def play(cups, moves):
    idx = 0
    max_cups = max(cups)
    for _ in tqdm(range(moves)):
        curr = cups[idx]
        rem = []
        for _ in range(3):
            i = (idx + 1)
            if i == len(cups):
                i = 0
                idx -= 1
            rem.append(cups.pop(i))

        goal = curr - 1
        while goal == 0 or goal in rem:
            goal -= 1
            if goal == -1:
                goal = max_cups
        goal_i = cups.index(goal) + 1
        for i in range(2, -1, -1):
            cups.insert(goal_i, rem[i])
        idx = (cups.index(curr) + 1) % len(cups)

    return cups

end = play(initial_cups[:], 100)
one = end.index(1)
s1 = "".join(str(end[(one + i) % len(end)]) for i in range(1, len(end)))

print("1:", s1)

cups2 = initial_cups[:] + [x for x in range(10, 1_000_000 + 1)]
end = play(cups2, 10_000_000)
one = end.index(1)
a, b = end[(one + 1) % len(end)], end[(one + 2) % len(end)]
print("2:", a * b)

"""
import java.util.*;

public class Day23 {

    static List<Integer> play(final List<Integer> cups, final int moves) {
        int idx = 0;
        int max_cups = cups.stream().max(Integer::compareTo).get();
        for (int x=0; x < moves; x++) {
            Integer curr = cups.get(idx);
            final ArrayList<Integer> rem = new ArrayList<>(3);
            for (int i=0; i < 3; i++) {
                int idx2 = idx + 1;
                if (idx2 == cups.size()) {
                    idx2 = 0;
                    idx -= 1;
                }
                rem.add(cups.remove(idx2));
            }
            Integer goal = curr - 1;
            while (goal == 0 || rem.contains(goal)) {
                goal -= 1;
                if (goal == -1) {
                    goal = max_cups;
                }
            }
            int goal_i = cups.indexOf(goal) + 1;
            for (int i=2; i >= 0; i--) {
                cups.add(goal_i, rem.get(i));
            }
            idx = (cups.indexOf(curr) + 1) % cups.size();
        }
        return cups;
    }

    public static void main(final String[] args) {
        final List<Integer> input = new ArrayList<>(Arrays.asList(6,4,3,7,1,9,2,5,8));
        //final List<Integer> end = play(new LinkedList<>(input), 100);
        //System.out.println(Arrays.toString(end.toArray()));
        final List<Integer> input2 = new ArrayList<>(input);
        for (int i=10; i < 1_000_001; i++) {
            input2.add(i);
        }
        final List<Integer> end = play(input2, 10_000_000);
        final int one = end.indexOf(1);
        long a = end.get((one + 1) % end.size());
        long b = end.get((one + 2) % end.size());
        System.out.println("2: " + (a*b));
    }
}
"""
