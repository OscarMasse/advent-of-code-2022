import operator
from dataclasses import dataclass, field
from typing import Optional

from utils import load_input

OPERATORS = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
}


@dataclass
class Monkey:
    items: list | None = None
    operator: Optional[operator] = None
    operation_number: int | str | None = None
    divisor: int | None = None
    recipient_monkey_if_true: Optional['Monkey'] = None
    recipient_monkey_if_false: Optional['Monkey'] = None
    business_level = 0

    def throw(self):
        if self.items[0] % self.divisor == 0:
            self.recipient_monkey_if_true.items.append(self.items[0])
            del self.items[0]
        else:
            self.recipient_monkey_if_false.items.append(self.items[0])
            del self.items[0]

    def inspect(self):
        self.items[0] = self.operator(
            self.items[0],
            self.operation_number
            if isinstance(self.operation_number, int)
            else self.items[0]
        )


def solve():
    monkeys = parse_monkeys()
    for _ in range(20):
        for monkey in monkeys:
            while monkey.items:
                monkey.business_level += 1
                monkey.inspect()
                # Relief
                monkey.items[0] = monkey.items[0] // 3
                monkey.throw()
    sorted_monkeys = sorted([monkey.business_level for monkey in monkeys], reverse=True)
    print(sorted_monkeys[0] * sorted_monkeys[1])


def parse_monkeys():
    monkeys = []
    input_ = load_input().split('\n\n')
    for _ in range(len(input_)):
        monkeys.append(Monkey())
    for index, chunk in enumerate(input_):
        monkey = monkeys[index]
        lines = chunk.splitlines()
        monkey.items = [int(item) for item in lines[1].replace("Starting items: ", "").split(", ")]
        split = lines[2].replace(" Operation: new = old ", "").split()
        monkey.operator = OPERATORS[split[0]]
        monkey.operation_number = int(split[1]) if split[1].isdigit() else split[1]
        monkey.divisor = int(lines[3].replace("  Test: divisible by ", ""))
        monkey.recipient_monkey_if_true = monkeys[int(lines[4].replace("    If true: throw to monkey ", ""))]
        monkey.recipient_monkey_if_false = monkeys[int(lines[5].replace("    If false: throw to monkey ", ""))]

    return monkeys


if __name__ == '__main__':
    solve()
