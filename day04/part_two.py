from utils import load_input


def solve():
    input_ = load_input()
    pairs = [tuple(list_sections(sections) for sections in line.split(',')) for line in input_.splitlines()]
    count = 0
    for first, second in pairs:
        if set(first).intersection(set(second)):
            count += 1

    print(count)


def list_sections(sections):
    split = sections.split('-')
    return [*range(int(split[0]), int(split[1]) + 1)]


if __name__ == '__main__':
    solve()
