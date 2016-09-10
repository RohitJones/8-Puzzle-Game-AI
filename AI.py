from main import *
from copy import deepcopy
from random import randint
from time import sleep

Previous_States = []

def heuristic_value(input_board):
    coordinates = {0: (0, 0), 1: (1, 0), 2: (2, 0),
                   3: (0, 1), 4: (1, 1), 5: (2, 1),
                   6: (0, 2), 7: (1, 2), 8: (2, 2)}

    def distance(n, m):
        x1, y1 = coordinates[n]
        x2, y2 = coordinates[m]
        return abs(x1 - x2) + abs(y1 - y2)

    value = 0
    for x in range(9):
        value += distance(input_board.index(x), x)

    return value


def astart(current_board=Board):
    previous_move = None
    while not is_solved(current_board):
        possible_states = []
        temp_list = possible_moves(current_board, previous_move)
        for each in temp_list:
            temp = iMove(each, current_board)
            possible_states.append((heuristic_value(temp), each, temp))

        possible_states.sort(key=lambda val: val[0])
        previous_move = possible_states[0][1]
        move(possible_states[0][1], current_board)
        display_refresh(current_board)
        sleep(0.030)

def hillclimbing(current_board=Board):
    if current_board in Previous_States:
        return
    else:
        Previous_States.append(current_board)

    while not is_solved(current_board):

        current_h_value = heuristic_value(current_board)
        possible_states = []
        temp_list = possible_moves(current_board)
        for each in temp_list:
            temp = iMove(each, current_board)
            possible_states.append((heuristic_value(temp), each, temp))

        possible_states.sort(key=lambda val: val[0])

        if possible_states[0][0] < current_h_value:
            move(possible_states[0][1], current_board)

        elif possible_states[0][0] == current_h_value:
            for each in possible_states:
                if each[0] == current_h_value:
                    hillclimbing(each[2])

        else:
            count = randint(5, 10)
            for x in range(count):
                init_game_temp = possible_moves(current_board)
                move(init_game_temp[randint(0, len(init_game_temp) - 1)], current_board)

        display_refresh(current_board)

    print(current_board)

def iMove(position, current_board=Board):
    def swap(pos_1, pos_2):
        local_board[pos_1], local_board[pos_2] = local_board[pos_2], local_board[pos_1]

    local_board = deepcopy(current_board)
    position = position.lower()
    current_pos = local_board.index(8)

    if position == 'down':
        swap(current_pos, (current_pos - 3))

    if position == 'up':
        swap(current_pos, (current_pos + 3))

    if position == 'right':
        swap(current_pos, (current_pos - 1))

    if position == 'left':
        swap(current_pos, (current_pos + 1))

    return local_board

if __name__ == "__main__":
    init_game(10)
    display_refresh()
    # hillclimbing()
    # print(Board)
    # input("start !")
    astart()
    # input("solved !")
    # print(Board)
    # temp = iMove('up')
    # print(temp)
    # print(Board)