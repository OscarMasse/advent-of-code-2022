from utils import load_input

# Rock: A, 1 pts
# Paper: B, 2 pts
# Scissors: C, 3 pts

# Win: Z, 6 pts
# Draw: Y, 3 pts
# Loss: X, 0 pts

INPUT_TO_SHAPE = {
    'A': 'rock',
    'B': 'paper',
    'C': 'scissors',
}
INPUT_TO_ACTION = {
    'X': 'lose',
    'Y': 'draw',
    'Z': 'win',
}
SHAPE_TO_POINTS = {'rock': 1, 'paper': 2, 'scissors': 3}
ACTION_TO_POINTS = {'lose': 0, 'draw': 3, 'win': 6}
WINNER_TO_LOSER = {'rock': 'scissors', 'paper': 'rock', 'scissors': 'paper'}
LOSER_TO_WINNER = {'rock': 'paper', 'paper': 'scissors', 'scissors': 'rock'}


def solve():
    input_ = load_input()
    scores = [compute_score(*line.split()) for line in input_.splitlines()]
    total = sum(scores)

    print(total)


def compute_score(enemy_input, player_input):
    enemy_shape = INPUT_TO_SHAPE[enemy_input]
    action = INPUT_TO_ACTION[player_input]

    # Draw
    player_shape = enemy_shape
    if action == 'lose':
        player_shape = WINNER_TO_LOSER[enemy_shape]
    elif action == 'win':
        player_shape = LOSER_TO_WINNER[enemy_shape]

    return SHAPE_TO_POINTS[player_shape] + ACTION_TO_POINTS[action]


if __name__ == '__main__':
    solve()
