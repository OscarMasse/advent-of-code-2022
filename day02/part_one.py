from utils import load_input

# Rock: A, X, 1 pts
# Paper: B, Y, 2 pts
# Scissors: C, Z, 3 pts

# Win: 6 pts
# Draw: 3 pts
# Loss: 0 pts

INPUT_TO_SHAPE = {
    'A': 'rock',
    'X': 'rock',
    'B': 'paper',
    'Y': 'paper',
    'C': 'scissors',
    'Z': 'scissors',
}
SHAPE_TO_POINTS = {'rock': 1, 'paper': 2, 'scissors': 3}
WINNER_TO_LOSER = {'rock': 'scissors', 'paper': 'rock', 'scissors': 'paper'}


def solve():
    input_ = load_input()
    scores = [compute_score(*line.split()) for line in input_.splitlines()]
    total = sum(scores)

    print(total)


def compute_score(enemy_input, player_input):
    enemy_shape = INPUT_TO_SHAPE[enemy_input]
    player_shape = INPUT_TO_SHAPE[player_input]

    result = 0
    if player_shape == enemy_shape:
        result = 3
    elif enemy_shape == WINNER_TO_LOSER[player_shape]:
        result = 6
    return SHAPE_TO_POINTS[player_shape] + result


if __name__ == '__main__':
    solve()
