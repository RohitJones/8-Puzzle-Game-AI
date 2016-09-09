from main import *
game_QUIT = False

def heuristic_value(input_board):
    value = 0
    Board.index(1) #should be 0


if __name__ == "__main__":
    init_game()
    display_refresh()

    while not is_solved() and not game_QUIT:
        keyboard_input()
        display_refresh()
