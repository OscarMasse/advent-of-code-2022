import operator
from dataclasses import dataclass, field
from typing import Optional

from utils import load_input


@dataclass
class Item:
    initial_value: int
    divisor_to_value: dict = field(default_factory=dict)

    def is_divisible(self, divisor):
        return self.divisor_to_value[divisor] == 0

    def add(self, number):
        for divisor, value in self.divisor_to_value.items():
            self.divisor_to_value[divisor] = (value + (number % divisor)) % divisor

    def multiply(self, number):
        for divisor, value in self.divisor_to_value.items():
            self.divisor_to_value[divisor] = (value * (number % divisor)) % divisor

    def square(self, _):
        for divisor, value in self.divisor_to_value.items():
            self.divisor_to_value[divisor] = (value * value) % divisor


@dataclass
class Monkey:
    items: list[Item] | None = None
    operator: Optional[operator] = None
    operation_number: int | str | None = None
    divisor: int | None = None
    recipient_monkey_if_true: Optional['Monkey'] = None
    recipient_monkey_if_false: Optional['Monkey'] = None
    business_level = 0

    def throw(self):
        if self.items[0].is_divisible(self.divisor):
            self.recipient_monkey_if_true.items.append(self.items[0])
            del self.items[0]
        else:
            self.recipient_monkey_if_false.items.append(self.items[0])
            del self.items[0]

    def inspect(self):
        self.operator(self.items[0], self.operation_number)


OPERATORS = {
    '+': Item.add,
    '*': Item.multiply,
}


def solve():
    monkeys = parse_monkeys()
    for round_count in range(1, 10_000 + 1):
        for monkey in monkeys:
            while monkey.items:
                # Item inspection
                monkey.business_level += 1
                monkey.inspect()
                monkey.throw()
        # if round_count in [1, 20, 1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000]:
        #     print(f"== After round {round_count} ==")
        #     for index, monkey in enumerate(monkeys):
        #         print(f"Monkey {index} inspected items {monkey.business_level} times.")

    sorted_monkeys = sorted([monkey.business_level for monkey in monkeys], reverse=True)
    print(sorted_monkeys[0] * sorted_monkeys[1])


def parse_monkeys():
    monkeys = []
    input_ = load_input().split('\n\n')
    # Create monkeys
    for _ in range(len(input_)):
        monkeys.append(Monkey())
    # Fill monkeys data
    for index, chunk in enumerate(input_):
        monkey = monkeys[index]
        lines = chunk.splitlines()
        monkey.items = [Item(int(item)) for item in lines[1].replace("Starting items: ", "").split(", ")]
        split = lines[2].replace(" Operation: new = old ", "").split()
        monkey.operator = OPERATORS[split[0]] if not split[1] == 'old' else Item.square
        monkey.operation_number = int(split[1]) if split[1].isdigit() else None
        monkey.divisor = int(lines[3].replace("  Test: divisible by ", ""))
        monkey.recipient_monkey_if_true = monkeys[int(lines[4].replace("    If true: throw to monkey ", ""))]
        monkey.recipient_monkey_if_false = monkeys[int(lines[5].replace("    If false: throw to monkey ", ""))]
    # Initialize items
    for monkey in monkeys:
        for item in monkey.items:
            for divisor in [m.divisor for m in monkeys]:
                item.divisor_to_value[divisor] = item.initial_value % divisor
    return monkeys


if __name__ == '__main__':
    solve()
