import pygame
from random import randint
from sys import exit

Board = [0 for useless_variable in range(9)]
Moves = ['down', 'up', 'right', 'left']
Tiles = []
game_QUIT = False
hints_enabled = False

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
    BLACK = 0, 0, 0

    def __init__(self, value):
        self.value = value

    def render_tile(self, output=screen):
        b_gfx_p = positions[Board.index(self.value)]  # board_gfx_position
        color = self.RED
        if position_is_correct(self.value):
            color = self.GREEN

        pygame.draw.rect(output, color, pygame.Rect(b_gfx_p))

        if hints_enabled:
            text_size = 217
            font = pygame.font.Font(None, text_size)
            ren = font.render(str(self.value), 0, color, self.BLACK)
            pygame.draw.rect(output, self.BLACK, pygame.Rect(b_gfx_p[0] + 25, b_gfx_p[1] + 25, 150, 150))
            screen.blit(ren, (b_gfx_p[0] + 34 + 25, b_gfx_p[1] + 30))
            pygame.draw.rect(output, color, pygame.Rect(b_gfx_p[0], b_gfx_p[1] + 175, 200, 20))

def init_game():
    global Tiles
    Tiles = [Tile(x + 1) for x in range(8)]
    print("inspection point !")
    for make_game_x in range(8):
        Board[make_game_x] = (make_game_x + 1)

    for x in range(10):
        init_game_temp = possible_moves()
        move(init_game_temp[randint(0, len(init_game_temp) - 1)])
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

    if position == 'down':
        swap(current_pos, (current_pos - 3))

    if position == 'up':
        swap(current_pos, (current_pos + 3))

    if position == 'right':
        swap(current_pos, (current_pos - 1))

    if position == 'left':
        swap(current_pos, (current_pos + 1))

def display_refresh():
    screen.fill((0, 0, 0))
    for each in Tiles:
        each.render_tile()
    pygame.display.flip()
    pygame.time.Clock().tick(60)
def keyboard_input():
    global hints_enabled
    for event in pygame.event.get():
        if is_solved():
            break

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and "up" in possible_moves():
                move("up")
            if event.key == pygame.K_DOWN and "down" in possible_moves():
                move("down")
            if event.key == pygame.K_LEFT and "left" in possible_moves():
                move("left")
            if event.key == pygame.K_RIGHT and "right" in possible_moves():
                move("right")

            if event.key == pygame.K_RSHIFT or event.key == pygame.K_CAPSLOCK:
                hints_enabled = True

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RSHIFT or event.key == pygame.K_CAPSLOCK:
                hints_enabled = False

        if event.type == pygame.QUIT:
            exit()


if __name__ == "__main__":
    init_game()
    display_refresh()
    while not is_solved():
        keyboard_input()
        display_refresh()
