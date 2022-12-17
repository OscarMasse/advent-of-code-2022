from utils import load_input


def solve():
    input_ = load_input()
    lines = input_.splitlines()
    scores = [compute_score(*group) for group in [lines[n:n + 3] for n in range(0, len(lines), 3)]]

    print(sum(scores))


def compute_score(rucksack1, rucksack2, rucksack3):
    common_item = list(set.intersection(*[set(list_) for list_ in [rucksack1, rucksack2, rucksack3]]))[0]

    if common_item.islower():
        return ord(common_item) - 96  # -96 = -ord('a') + 1

    return ord(common_item) - 38  # -38 = -ord('A') + 27


if __name__ == '__main__':
    solve()
