from random import randint

Board = [0 for useless_variable in range(9)]
bak_board = [i for i in range(10)]

Moves = ['up', 'down', 'left', 'right']


def is_solved():
    for checker_x in range(8):
        if Board[checker_x] != (checker_x + 1):
            return False

    return True


def init_game():
    for make_game_x in range(8):
        Board[make_game_x] = (make_game_x + 1)

    for x in range(100):
        temp = possible_moves()
        move(temp[randint(0, len(temp) - 1)])


def possible_moves():
    possible_moves_temp = [True, True, True, True]

    upper_edge = [0, 1, 2]
    left_edge = [0, 3, 6]
    lower_edge = [6, 7, 8]
    right_edge = [2, 5, 8]

    pos = Board.index(0)

    if pos in upper_edge:
        possible_moves_temp[0] = False
    if pos in lower_edge:
        possible_moves_temp[1] = False
    if pos in left_edge:
        possible_moves_temp[2] = False
    if pos in right_edge:
        possible_moves_temp[3] = False

    return [Moves[x] for x in range(4) if possible_moves_temp[x] is True]


def move(position):
    def swap(pos_1, pos_2):
        global Board
        Board[pos_1], Board[pos_2] = Board[pos_2], Board[pos_1]

    position = position.lower()
    current_pos = Board.index(0)

    if position == 'up':
        swap(current_pos, (current_pos - 3))

    if position == 'down':
        swap(current_pos, (current_pos + 3))

    if position == 'left':
        swap(current_pos, (current_pos - 1))

    if position == 'right':
        swap(current_pos, (current_pos + 1))


if __name__ == "__main__":
    init_game()
    while not is_solved():
        print(Board)
        move(input("Enter position: "))

    print("Solved !!!!")
