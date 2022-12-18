from utils import load_input

CYCLES_TO_MEASURE = [20, 60, 100, 140, 180, 220]


def solve():
    cycle_count = 0
    register = 1
    signal_strength_sum = 0

    for line in load_input().splitlines():
        match line.split():
            case ["addx", value]:
                cycle_count += 1
                signal_strength_sum += measure(cycle_count, register)
                cycle_count += 1
                signal_strength_sum += measure(cycle_count, register)
                register += int(value)
            case _:
                cycle_count += 1
                signal_strength_sum += measure(cycle_count, register)

    print(signal_strength_sum)


def measure(cycle_count, register):
    if cycle_count in CYCLES_TO_MEASURE:
        return cycle_count * register
    return 0


if __name__ == '__main__':
    solve()
