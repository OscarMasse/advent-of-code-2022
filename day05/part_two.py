from utils import load_input


def solve():
    input_ = load_input()
    split = input_.split('\n\n')
    stacks = [
        to_stack(list_[::-1])
        for list_
        in list(
            map(
                list,
                zip(*[
                    [
                        line[i:i + 4]
                        for i in range(0, len(line), 4)
                    ]
                    for line in split[0].splitlines()
                ])
            )
        )
    ]

    moves = [[int(s) for s in line.split() if s.isdigit()] for line in split[1].splitlines()]
    for count, from_, to in moves:
        from_ -= 1
        to -= 1
        from_stack = stacks[from_]
        to_stack_ = stacks[to]
        to_stack_.extend(from_stack[-count:])
        del from_stack[-count:]

    print(''.join([list_[-1:][0] for list_ in stacks]))


def to_stack(list_):
    stack = []
    for element in [element for element in list_[1:] if element.replace(' ', '')]:
        if all(char in element for char in ['[', ']']):
            for char in '[] ':
                element = element.replace(char, '')
        stack.append(element)
    return stack


if __name__ == '__main__':
    solve()
