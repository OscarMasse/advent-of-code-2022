from dataclasses import field, dataclass

from utils import load_input


@dataclass
class Cpu:
    cycle_count: int = 0
    register: int = 1
    crt: list = field(default_factory=list)

    @property
    def crt_cursor(self):
        return (self.cycle_count - 1) % 40

    def cycle(self):
        self.cycle_count += 1
        self.draw()

    def draw(self):
        self.crt.append("#" if self.is_sprite_over_crt_cursor() else ".")

    def is_sprite_over_crt_cursor(self):
        return abs(self.register - self.crt_cursor) < 2


def solve():
    cpu = Cpu()

    for line in load_input().splitlines():
        match line.split():
            case ["addx", value]:
                cpu.cycle()
                cpu.cycle()
                cpu.register += int(value)
            case _:
                cpu.cycle()

    for line in split(cpu.crt, 6):
        print(''.join(line))


def split(a, n):
    k, m = divmod(len(a), n)
    return (a[i * k + min(i, m):(i + 1) * k + min(i + 1, m)] for i in range(n))


if __name__ == '__main__':
    solve()
