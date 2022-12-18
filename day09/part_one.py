from math import sqrt

from utils import load_input


def compute_distance(x1, x2, y1, y2):
    return sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)


class Tail:
    x: int = 0
    y: int = 0
    visited_positions: set

    def __init__(self):
        self.visited_positions = set(tuple([0, 0]))

    def follow(self, x, y):
        current_distance = compute_distance(x, self.x, y, self.y)
        if current_distance < 2:
            return

        available_positions = (
            (self.x, self.y + 1),  # U
            (self.x + 1, self.y),  # R
            (self.x, self.y - 1),  # D
            (self.x - 1, self.y),  # L
            (self.x + 1, self.y + 1),  # UR
            (self.x - 1, self.y + 1),  # UL
            (self.x + 1, self.y - 1),  # DR
            (self.x - 1, self.y - 1),  # DL
        )
        closest_position = (self.x, self.y)
        closest_distance = current_distance
        for position in available_positions:
            distance = compute_distance(position[0], x, position[1], y)
            if distance < closest_distance:
                closest_position = position
                closest_distance = distance

        self.move(closest_position[0], closest_position[1])

    def move(self, x, y):
        self.x = x
        self.y = y
        self.visited_positions.add((x, y))


class Head:
    x: int = 0
    y: int = 0
    tail: Tail = Tail()

    def __init__(self):
        self.DIRECTION_TO_MOVE = {
            'U': self.move_up,
            'D': self.move_down,
            'L': self.move_left,
            'R': self.move_right,
        }

    def move(self, direction, distance):
        for _ in range(distance):
            self.DIRECTION_TO_MOVE[direction]()
            self.tail.follow(self.x, self.y)

    def move_up(self):
        self.y += 1

    def move_down(self):
        self.y -= 1

    def move_left(self):
        self.x -= 1

    def move_right(self):
        self.x += 1


def solve():
    moves = [[line.split()[0], int(line.split()[1])] for line in load_input().splitlines()]
    head = Head()

    for direction, distance in moves:
        head.move(direction, distance)

    print(len(head.tail.visited_positions))


if __name__ == '__main__':
    solve()
