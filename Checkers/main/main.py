import pygame
from checkers.constants import width, height, square_size, CREAM, DARK
from checkers.board import *
from checkers.game import Game

FPS = 60
win = pygame.display.set_mode((width, height))
pygame.display.set_caption('Checkers')

def get_row_col_from_mouse(pos):
    x, y = pos
    row = y // square_size
    col = x // square_size
    return row, col

def main():
    run = True
    clock = pygame.time.Clock()
    game = Game(win)
    
    while run:
        clock.tick(FPS)

        # AI Turn Execution (Let's make DARK the AI)
        if game.turn == DARK:
            # Depth 3 means looking 3 moves ahead. 
            # High depths (4+) might lag because Python's deepcopy can be slow.
            value, new_board = minimax(game.get_board(), 3, True, game)
            if new_board:
                game.ai_move(new_board)
            else:
                print("No moves left! Game Over.")

        if game.winner() is not None:
            print(f"The winner is: {game.winner()}")

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            # Only listen to mouse clicks if it's the human's turn (CREAM)
            if event.type == pygame.MOUSEBUTTONDOWN and game.turn == CREAM:
                pos = pygame.mouse.get_pos()
                row, col = get_row_col_from_mouse(pos)
                game.select(row, col)

        game.update()
        
    pygame.quit()

main()