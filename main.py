import pygame
from random import randint

Board = [0 for useless_variable in range(9)]
Moves = ['up', 'down', 'left', 'right']
Tiles = None

pygame.init()
resolution = 620, 620
screen = pygame.display.set_mode(resolution)

positions = {
    0: (5, 5, 200, 200),
    1: (210, 5, 200, 200),
    2: (415, 5, 200, 200),

    3: (5, 210, 200, 200),
    4: (210, 210, 200, 200),
    5: (415, 210, 200, 200),

    6: (5, 415, 200, 200),
    7: (210, 415, 200, 200),
    8: (415, 415, 200, 200)
}


class Tile:
    GREEN = 0, 255, 0
    RED = 255, 0, 0

    def __init__(self, value):
        self.value = value

    def render_tile(self, output=screen):
        board_gfx_position = positions[Board.index(self.value)]
        color = self.RED
        if position_is_correct(self.value):
            color = self.GREEN

        pygame.draw.rect(output, color, pygame.Rect(board_gfx_position))


def position_is_correct(value):
    if value == 0 and Board[9] == 0:
        return True

    elif Board[value - 1] == value:
        return True

    return False


def is_solved():
    for checker_x in range(8):
        if Board[checker_x] != (checker_x + 1):
            return False

    return True


def init_game():
    global Tiles
    Tiles = [Tile(x+1) for x in range(8)]
    print("inspection point !")
    for make_game_x in range(8):
        Board[make_game_x] = (make_game_x + 1)

    for x in range(3):
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


def display_refresh():
    screen.fill((0, 0, 0))
    for each in Tiles:
        each.render_tile()
    pygame.display.flip()
    pygame.time.Clock().tick(60)


if __name__ == "__main__":
    init_game()
    display_refresh()
    while not is_solved():
        print(Board)
        move(input("Enter position: "))
        display_refresh()

    input("Solved !!!!")
