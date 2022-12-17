from utils import load_input


def solve():
    input_ = load_input()
    scores = [compute_score(line) for line in input_.splitlines()]

    print(sum(scores))


def compute_score(list_):
    compartment1, compartment2 = split_list(list_)

    common_item = next((item for item in set(compartment1) if item in set(compartment2)), None)

    if common_item.islower():
        return ord(common_item) - 96  # -96 = -ord('a') + 1

    return ord(common_item) - 38  # -38 = -ord('A') + 27


def split_list(list_):
    half = len(list_) // 2
    return list_[:half], list_[half:]


if __name__ == '__main__':
    solve()
