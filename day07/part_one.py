from dataclasses import dataclass, field

from utils import load_input


@dataclass
class Directory:
    name: str
    children: list = field(default_factory=list)

    @property
    def size(self):
        if not self.children:
            return 0

        return sum([child.size for child in self.children])

    @property
    def child_directories(self):
        return [child for child in self.children if isinstance(child, Directory)]

    def get_child_by_name(self, name):
        return next(child for child in self.children if child.name == name)


@dataclass
class File:
    name: str
    size: int


CD = "$ cd "
CD_PARENT = "$ cd .."
LS = "$ ls"
MAX_SIZE = 100_000


def solve():
    input_ = load_input()
    directories = parse_directories(input_)
    print(sum([directory.size for directory in directories if directory.size <= MAX_SIZE]))


def parse_directories(input_):
    root = Directory('/')
    directories = [root]
    path = []
    for line in input_.splitlines():
        match line.split():
            case ["$", "cd", ".."]:
                path.pop()
            case ["$", "cd", dir_name]:
                path.append(path[-1].get_child_by_name(dir_name) if path else root)
            case ["$", "ls"]:
                pass
            case ["dir", dir_name]:
                directory = Directory(dir_name)
                path[-1].children.append(directory)
                directories.append(directory)
            case [size, file_name]:
                path[-1].children.append(File(file_name, int(size)))
    return directories


if __name__ == '__main__':
    solve()
