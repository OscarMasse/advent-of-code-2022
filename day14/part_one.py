import itertools
from dataclasses import dataclass
from typing import Iterable, Iterator

from utils import load_input


@dataclass(frozen=True)
class Point:
    x: int
    y: int

    @classmethod
    def from_str_position(cls, position) -> 'Point':
        x, y = position.split(",")
        return cls(int(x), int(y))

    @staticmethod
    def interpolate(points: list['Point']) -> list['Point']:
        if len(points) == 1:
            return points
        output = []
        for i in range(1, len(points)):
            a = points[i - 1]
            b = points[i]
            if a.x == b.x:
                y_min = min(a.y, b.y)
                y_max = max(a.y, b.y)
                output.extend([Point(a.x, y) for y in range(y_min, y_max + 1)])
            else:
                x_min = min(a.x, b.x)
                x_max = max(a.x, b.x)
                output.extend([Point(x, a.y) for x in range(x_min, x_max + 1)])
        return output


class Screen(Iterable):
    @dataclass
    class Line(Iterable):
        elements: list
        offset: int = 0

        @property
        def x_min(self):
            return -self.offset

        @property
        def x_max(self):
            return -self.offset + len(self.elements) - 1

        def __iter__(self) -> Iterator:
            for element in self.elements:
                yield element

        def __getitem__(self, index: int):
            return self.elements[index + self.offset]

        def __setitem__(self, key, value):
            self.elements[key + self.offset] = value

        def __len__(self):
            return len(self.elements)

        def __str__(self):
            return ''.join(self.elements)

    matrix: list[Line]
    offset: int = 0

    def __init__(self, input_: str, source: Point = Point(500, 0)):
        rock_paths = [
            [Point.from_str_position(position) for position in line.split(" -> ")]
            for line in input_.splitlines()
        ]
        # Init screen
        points = tuple(itertools.chain.from_iterable(rock_paths))
        xs = [point.x for point in points]
        x_min = min(xs) - 1
        x_max = max(xs) + 1
        ys = [point.y for point in points]
        self.offset = y_min = 0
        y_max = max(ys) + 1
        self.matrix = [self.Line(['.' for _ in range(x_min, x_max + 1)], offset=-x_min) for _ in
                       range(y_min, y_max + 1)]

        # Place source
        self[source.y][source.x] = '+'

        # Place rocks
        for rock_path in rock_paths:
            for point in Point.interpolate(rock_path):
                self[point] = '#'

    def __iter__(self) -> Iterator:
        for line in self.matrix:
            yield line

    def __getitem__(self, key: int | Point):
        if isinstance(key, Point):
            return self.matrix[key.y + self.offset][key.x]
        return self.matrix[key + self.offset]

    def __setitem__(self, key: int | Point, value):
        if isinstance(key, Point):
            self.matrix[key.y + self.offset][key.x] = value
            return
        self.matrix[key + self.offset] = value

    @property
    def y_min(self) -> int:
        return -self.offset

    @property
    def y_max(self) -> int:
        return -self.offset + len(self.matrix) - 1

    def print(self, count: int | None):
        first_line = self[0]
        print(f"   [{first_line.x_min}-{first_line.x_max}{f' - Sand units: {count}' if count else ''}]")
        for index, line in enumerate(self.matrix, start=self.offset):
            print(f"{'{:3d}'.format(index)} {str(line)}")
        print('\n')


def solve():
    source = Point(500, 0)
    screen = Screen(load_input(), source)
    sand_count = 0
    running = True
    while running:
        sand_unit = source
        while True:
            # Abyss
            if sand_unit.y == screen.y_max:
                running = False
                break

            # Bottom
            next_position = Point(sand_unit.x, sand_unit.y + 1)
            if screen[next_position] == '.':
                sand_unit = next_position
                continue

            # Bottom left
            next_position = Point(sand_unit.x - 1, sand_unit.y + 1)
            if screen[next_position] == '.':
                sand_unit = next_position
                continue

            # Bottom right
            next_position = Point(sand_unit.x + 1, sand_unit.y + 1)
            if screen[next_position] == '.':
                sand_unit = next_position
                continue

            # Idle
            screen[sand_unit] = 'o'
            sand_count += 1
            screen.print(sand_count)
            break

    print(sand_count)


if __name__ == '__main__':
    solve()
