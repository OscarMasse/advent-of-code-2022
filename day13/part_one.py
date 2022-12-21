import json
from enum import Enum
from itertools import zip_longest

from utils import load_input


class Result(int, Enum):
    ORDERED = -1
    EQUAL = 0
    UNORDERED = 1


def solve():
    pairs = [[json.loads(line) for line in chunk.splitlines()] for chunk in load_input().split("\n\n")]
    indexes = []

    for index, (left, right) in enumerate(pairs, start=1):
        if compare(left, right) == Result.ORDERED:
            indexes.append(index)
            continue

    print(sum(indexes))


def compare(left, right):
    # Mixed type case
    left_type = type(left)
    right_type = type(right)
    if not left_type == right_type:
        if left_type == int:
            left = [left]
        if right_type == int:
            right = [right]

    # Int case
    if isinstance(left, int) and isinstance(right, int):
        if left == right:
            return Result.EQUAL
        elif left < right:
            return Result.ORDERED
        else:
            return Result.UNORDERED

    # List case
    if isinstance(left, list) and isinstance(right, list):
        for left_child, right_child in zip_longest(left, right):
            if left_child is None:
                return Result.ORDERED
            if right_child is None:
                return Result.UNORDERED
            result = compare(left_child, right_child)
            if result == Result.EQUAL:
                continue
            else:
                return result
        return Result.EQUAL


if __name__ == '__main__':
    solve()
