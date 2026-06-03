import pygame
from .constants import DARK_BROWN, rows, cols, LIGHT_BROWN, square_size, CREAM, DARK
from .piece import piece

class Board:
    def __init__(self):
        self.board = []
        self.red_left = self.white_left = 12
        self.red_kings = self.white_kings = 0
        self.create_board()

    def draw_squares(self, win):
        win.fill(DARK_BROWN)
        for row in range(rows):
            for col in range(row%2, cols, 2):
                pygame.draw.rect(win, LIGHT_BROWN, (col*square_size, row*square_size, square_size, square_size))

    def move(self, piece, row, col):
        self.board[piece.row][piece.col], self.board[row][col] = self.board[row][col], self.board[piece.row][piece.col]
        piece.move(row,col)

        if row == 0 or row == rows-1:
            piece.make_king()
            if piece.color == LIGHT_BROWN:
                self.white_kings+=1
            else: self.red_kings+=1

    def get_piece(self, row, col):
        return self.board[row][col]

    def create_board(self):
        for row in range(rows):
            self.board.append([])
            for col in range(cols):
                if col%2 == ((row+1)%2):
                    if row<3:
                        self.board[row].append(piece(row, col, DARK))
                    elif row>4:
                        self.board[row].append(piece(row, col, CREAM))
                    else:
                        self.board[row].append(0)
                else:
                    self.board[row].append(0)

    def draw(self, win):
        self.draw_squares(win)
        for row in range(rows):
            for col in range(cols):
                piece = self.board[row][col]
                if piece!=0:
                    piece.draw(win)

    def remove(self, pieces):
        for piece in pieces:
            self.board[piece.row][piece.col] = 0
            if piece!=0:
                if piece.color == CREAM:
                    self.red_left -= 1
                else:
                    self.white_left -= 1

    def winner(self):
        if self.red_left<=0: return DARK
        elif self.white_left<=0: return CREAM

        return None

    def get_valid_moves(self, piece):
        moves = {}
        left = piece.col-1
        right = piece.col+1
        row = piece.row

        if piece.color==CREAM or piece.king:
            moves.update(self._traverse_left(row-1, max(row-3,-1), -1, piece.color, left))
            moves.update(self._traverse_right(row-1, max(row-3,-1), -1, piece.color, right))

        if piece.color==DARK or piece.king:
            moves.update(self._traverse_left(row+1, min(row+3,rows), 1, piece.color, left))
            moves.update(self._traverse_right(row+1, min(row+3,rows), 1, piece.color, right))
        
        return moves

    def _traverse_left(self, start, stop, step, color, left, skipped=[]):
        moves = {}
        last = []
        for r in range(start, stop, step):
            if left<0:
                break

            current = self.board[r][left] 
            if current==0:
                if skipped and not last:
                    break
                elif skipped:
                    moves[(r,left)] = last + skipped
                else:
                    moves[(r,left)] = last

                if last:
                    if step == -1:
                        row = max(r-3,0)
                    else:
                        row = min(r+3, rows)
                    moves.update(self._traverse_left(r+step, row, step, color, left-1,skipped=last))
                    moves.update(self._traverse_right(r+step, row, step, color, left+1,skipped=last))
                break
            elif current.color == color:
                break
            else:
                last = [current]
            
            left -= 1
        return moves

    def _traverse_right(self, start, stop, step, color, right, skipped=[]):
        moves = {}
        last = []
        for r in range(start, stop, step):
            if right>=cols   :
                break

            current = self.board[r][right]
            if current==0:
                if skipped and not last:
                    break
                elif skipped:
                    moves[(r,right)] = last + skipped
                else:
                    moves[r,right] = last

                if last:
                    if step == -1:
                        row = max(r-3,0)
                    else:
                        row = min(r+3, rows)
                    moves.update(self._traverse_left(r+step, row, step, color, right-1 ,skipped=last))
                    moves.update(self._traverse_right(r+step, row, step, color, right+1,skipped=last))
                break
            elif current.color == color:
                break
            else:
                last = [current]
            
            right += 1
    
        return moves
    
    def evaluate(self):
        # We assume the AI is playing as DARK (maximizing) and the player is CREAM (minimizing)
        # A king is worth more than a regular piece (e.g., +0.5 weight)
        return self.white_left - self.red_left + (self.white_kings * 0.5 - self.red_kings * 0.5)

    def get_all_pieces(self, color):
        pieces = []
        for row in self.board:
            for piece in row:
                if piece != 0 and piece.color == color:
                    pieces.append(piece)
        return pieces
    
from copy import deepcopy

def minimax(position, depth, max_player, game):
    """
    position: The current Board object state
    depth: How many moves ahead the AI looks
    max_player: Boolean (True if optimizing for AI, False if optimizing for human)
    """
    if depth == 0 or position.winner() is not None:
        return position.evaluate(), position
    
    if max_player:
        maxEval = float('-inf')
        best_move = None
        for move in get_all_moves(position, DARK, game):
            evaluation = minimax(move, depth - 1, False, game)[0]
            maxEval = max(maxEval, evaluation)
            if maxEval == evaluation:
                best_move = move
        return maxEval, best_move
    else:
        minEval = float('inf')
        best_move = None
        for move in get_all_moves(position, CREAM, game):
            evaluation = minimax(move, depth - 1, True, game)[0]
            minEval = min(minEval, evaluation)
            if minEval == evaluation:
                best_move = move
        return minEval, best_move


def simulate_move(piece, move, board, skip):
    """Executes a move on a deep-copied temporary board."""
    board.move(piece, move[0], move[1])
    if skip:
        board.remove(skip)
    return board


def get_all_moves(board, color, game):
    """Finds all simulated board outcomes for every valid move of a color."""
    moves = []
    for piece in board.get_all_pieces(color):
        valid_moves = board.get_valid_moves(piece)
        for move, skip in valid_moves.items():
            # Deepcopy clones the board so we don't disrupt the real game state
            temp_board = deepcopy(board)
            temp_piece = temp_board.get_piece(piece.row, piece.col)
            new_board = simulate_move(temp_piece, move, temp_board, skip)
            moves.append(new_board)
            
    return moves