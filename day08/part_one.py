from dataclasses import dataclass

from utils import load_input


@dataclass
class Tree:
    height: int
    is_visible: bool = False


def solve():
    input_ = load_input()
    forest = [[Tree(height) for height in line] for line in input_.splitlines()]
    parse_visible_trees(forest)
    forest = [line[::-1] for line in forest]
    parse_visible_trees(forest)
    forest = list(map(list, zip(*forest)))
    parse_visible_trees(forest)
    forest = [line[::-1] for line in forest]
    parse_visible_trees(forest)
    print(sum([sum([int(tree.is_visible) for tree in line]) for line in forest]))


def parse_visible_trees(forest):
    for line in forest:
        max_height = line[0].height
        line[0].is_visible = True
        for tree in line[1:]:
            if tree.height > max_height:
                tree.is_visible = True
                max_height = tree.height


if __name__ == '__main__':
    solve()
