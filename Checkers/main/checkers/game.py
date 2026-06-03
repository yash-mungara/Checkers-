import pygame
from .board import Board
from .constants import CREAM, DARK, GOLD, square_size, black
class Game:
    def __init__(self, win):
        self._init()
        self.win = win

    def update(self):
        self.board.draw(self.win)
        self.draw_valid_moves(self.valid_moves)
        pygame.display.update()

    def _init(self):
        self.selected = None
        self.board = Board()
        self.turn = CREAM
        self.valid_moves = {}
        
    def reset(self):
        self._init()

    def select(self, row, col):
        piece = self.board.get_piece(row, col)

        if self.selected:
            if (row, col) in self.valid_moves:
                self._move(row, col)
                return True

            self.selected = None
            self.valid_moves = {}

        if piece != 0 and piece.color == self.turn:
            self.selected = piece
            self.valid_moves = self.board.get_valid_moves(piece)
            return True

        return False

    def winner(self):
        return self.board.winner()

    def _move(self, row, col):
        piece = self.board.get_piece(row,col)
        if self.selected and piece==0 and (row,col) in self.valid_moves:
            self.board.move(self.selected, row, col)
            skipped = self.valid_moves[(row,col)]
            if skipped:
                self.board.remove(skipped)
            self.change_turn()
        else:
            return False
        
        return True 
    
    def draw_valid_moves(self, moves):
        for move in moves:
            row, col = move
            pygame.draw.circle(self.win, black, (col*square_size + square_size//2, row*square_size + square_size//2),15)


    def change_turn(self):
        self.valid_moves = {}
        if self.turn == CREAM:
            self.turn = DARK
        else: self.turn = CREAM  

    def get_board(self):
        return self.board

    def ai_move(self, board):
        self.board = board
        self.change_turn() 