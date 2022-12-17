from utils import load_input


def solve(n=1):
    input_ = load_input()
    sums = [sum([int(s) for s in elf.splitlines()]) for elf in input_.split('\n\n')]
    n_top = []

    for _ in range(n):
        max_ = max(sums)
        n_top.append(max_)
        sums.remove(max_)

    print(sum(n_top))


if __name__ == '__main__':
    solve()
