from day07.part_one import parse_directories
from utils import load_input

TOTAL_SPACE = 70_000_000
REQUIRED_SPACE = 30_000_000


def solve():
    input_ = load_input()
    directories = parse_directories(input_)
    used_space = max([directory.size for directory in directories])
    space_to_clear = REQUIRED_SPACE - (TOTAL_SPACE - used_space)
    print(min([directory.size for directory in directories if directory.size >= space_to_clear]))


if __name__ == '__main__':
    solve()
