from __future__ import annotations

from bisect import insort
from dataclasses import dataclass

from utils import load_input


@dataclass(frozen=True)
class Point:
    x: int
    y: int


@dataclass(unsafe_hash=True)
class Node:
    parent: Node | None
    position: Point
    cost: int = 0
    heuristic: int = 0

    @property
    def x(self):
        return self.position.x

    @property
    def y(self):
        return self.position.y

    @property
    def total_cost(self):
        return self.cost + self.heuristic

    def __eq__(self, other):
        return self.position == other.position


def solve():
    height_map = [line for line in load_input().splitlines()]

    starts = find_starts(height_map)
    goal = find_goal(height_map)

    path = a_star(height_map, starts, goal)

    # print_arrow_map(goal, height_map, path)
    # print_letter_map(goal, height_map, path)
    # print_capital_letter_map(goal, height_map, path)
    print(len(path) - 1)


def a_star(height_map, starts, goal):
    open_list: list[Node] = starts
    closed_list: list[Node] = []
    while open_list:
        current = open_list.pop(0)
        closed_list.append(current)

        # Found the goal
        if current == goal:
            path = []
            node = current
            while node:
                path.append(node)
                node = node.parent
            return path[::-1]

        for neighbour in get_neighbours(current, height_map, closed_list):
            neighbour.cost = current.cost + 1
            neighbour.heuristic = neighbour.cost + distance(neighbour, goal)

            # Check if neighbour exists in open_list
            index = next((index for index, node in enumerate(open_list) if node == neighbour), None)
            if index:
                # Exists with lower cost
                if open_list[index].cost < neighbour.cost:
                    continue
                # Exists with higher cost
                del open_list[index]

            insort(open_list, neighbour, key=lambda x: x.heuristic)


def find_starts(height_map):
    starts = [find_start(height_map)]
    for y, line in enumerate(height_map):
        if 'a' in line:
            starts.append(Node(None, Point(line.index('a'), y)))
    return starts


def find_start(height_map):
    return Node(None, find(height_map, 'S'))


def find_goal(height_map):
    return Node(None, find(height_map, 'E'))


def get_neighbours(current: Node, height_map, closed_list) -> list[Node]:
    neighbours = []
    up = Node(current, Point(current.x, current.y - 1))
    down = Node(current, Point(current.x, current.y + 1))
    left = Node(current, Point(current.x - 1, current.y))
    right = Node(current, Point(current.x + 1, current.y))
    for neighbour in [up, down, left, right]:
        if (
                is_valid(neighbour, height_map)
                and is_reachable(current, neighbour, height_map)
                and neighbour.position not in [node.position for node in closed_list]
        ):
            neighbours.append(neighbour)
    return neighbours


def is_valid(node, height_map):
    max_x = len(height_map[0])
    max_y = len(height_map)
    if not (0 <= node.x < max_x and 0 <= node.y < max_y):
        return False
    return True


def is_reachable(current, destination, height_map):
    current_height = ord(height_map[current.y][current.x].replace("S", "a").replace("E", "z"))
    destination_height = ord(height_map[destination.y][destination.x].replace("S", "a").replace("E", "z"))
    return destination_height <= current_height + 1


def distance(a: Node | Point, b: Node | Point):
    return abs(b.x - a.x + b.y - a.y)


def find(height_map, letter):
    for y, line in enumerate(height_map):
        if letter in line:
            return Point(line.index(letter), y)
    print(f"Letter {letter} not found in height map.")


def print_arrow_map(goal, height_map, path):
    map_ = [['.' for _ in range(len(height_map[0]))] for _ in range(len(height_map))]
    map_[goal.y][goal.x] = 'E'
    for index, point in enumerate(path):
        if not index:
            continue
        previous = path[index - 1]
        if previous.x < point.x:
            direction = '→'
        elif previous.x > point.x:
            direction = '←'
        elif previous.y < point.y:
            direction = '↓'
        elif previous.y > point.y:
            direction = '↑'
        map_[previous.y][previous.x] = direction
    for line in map_:
        print(''.join(line))


def print_letter_map(goal, height_map, path):
    map_ = [['.' for _ in range(len(height_map[0]))] for _ in range(len(height_map))]
    for point in path:
        map_[point.y][point.x] = height_map[point.y][point.x]
    map_[path[0].y][path[0].x] = 'S'
    map_[goal.y][goal.x] = 'E'
    for line in map_:
        print(''.join(line))


def print_capital_letter_map(goal, height_map, path):
    map_ = [[char for char in line] for line in height_map]
    for point in path:
        map_[point.y][point.x] = height_map[point.y][point.x].upper()
        map_[path[0].y][path[0].x] = 'S'
        map_[goal.y][goal.x] = 'E'
    for line in map_:
        print(''.join(line))


if __name__ == '__main__':
    solve()
