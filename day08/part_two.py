from utils import load_input


def solve():
    input_ = load_input()
    forest = [[int(height) for height in line] for line in input_.splitlines()]
    scenic_score = parse_scenic_score(forest)
    print(scenic_score)


def parse_scenic_score(forest):
    scenic_score = 0
    for y in range(1, len(forest) - 1):
        for x in range(1, len(forest[0]) - 1):
            current_height = forest[y][x]
            score = 1
            for tree_heights in [
                forest[y][x + 1:],
                forest[y][:x][::-1],
                [forest[j][x] for j in range(y + 1, len(forest))],
                [forest[j][x] for j in range(y - 1, -1, -1)],
            ]:
                score *= compute_score(current_height, tree_heights)

            scenic_score = max(scenic_score, score)

    return scenic_score


def compute_score(height, tree_heights):
    score = 0
    for tree_height in tree_heights:
        score += 1
        if tree_height >= height:
            break
    return score


if __name__ == '__main__':
    solve()
