from utils import load_input


def solve(end_index=4):
    input_ = load_input()
    start_index = 0
    while end_index < len(input_) and not are_char_different(input_[start_index:end_index]):
        start_index += 1
        end_index += 1

    print(end_index)


def are_char_different(str_):
    for char in str_:
        if str_.count(char) > 1:
            return False

    return True if str_ else False


if __name__ == '__main__':
    solve()
