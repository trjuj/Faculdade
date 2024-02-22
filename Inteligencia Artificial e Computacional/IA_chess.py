# João Lucas Mota Nogueira da Costa
# João Luís Chiarelotto Crema

import chess
import chess.svg
import threading
import math

from PyQt5.QtSvg import QSvgWidget
from PyQt5.QtWidgets import QApplication, QWidget

OPENINGS = {
    'e2e4': 'King\'s Opening',
    'e2e4 e7e5': 'Open Game',
    'e2e4 c7c5': 'Sicilian Defense'
}

def clear_transposition_table():
    """
    Limpa a tabela de transposicao.
    """
    global transposition_table
    transposition_table = {}

def get_opening_move(board):
    """
    Retorna um movimento de uma abertura predefinida, se disponivel.
    """
    moves = board.move_stack
    move_strs = [str(move) for move in moves]
    history = ' '.join(move_strs)

    for opening_moves, name in OPENINGS.items():
        if history in opening_moves:
            next_move = opening_moves[len(history):].strip().split()[0]
            return chess.Move.from_uci(next_move)
    return None

def get_best_move(board, depth):
    """
    Obtem o melhor movimento para a posicao atual.
    """
    # Primeiro, verifique as aberturas predefinidas
    opening_move = get_opening_move(board)
    if opening_move:
        return opening_move

    # Se nenhum movimento de abertura foi encontrado, use alpha-beta
    return alphabeta(board, depth)

def evaluate_board(board):
    """
    Avalia o tabuleiro do ponto de vista do jogador das brancas.
    """

    pawn_positions = [0, 0.5, 1, 1.5, 1.5, 1, 0.5, 0,
                      0.5, 1, 1.5, 2, 2, 1.5, 1, 0.5,
                      1, 1.5, 2, 2.5, 2.5, 2, 1.5, 1,
                      1, 2, 2.5, 3, 3, 2.5, 2, 1,
                      1.5, 2, 2.5, 3, 3, 2.5, 2, 1.5,
                      1.5, 2, 2.5, 3, 3, 2.5, 2, 1.5,
                      1, 1.5, 2, 2.5, 2.5, 2, 1.5, 1,
                      0.5, 1, 1.5, 2, 2, 1.5, 1, 0.5]

    knight_positions = [-5,-4,-3,-3,-3,-3,-4,-5,
                        -4,-2, 0, 0, 0, 0,-2,-4,
                        -3, 0, 1, 1.5, 1.5, 1, 0,-3,
                        -3, 0.5, 1.5, 2, 2, 1.5, 0.5,-3,
                        -3, 0, 1.5, 2, 2, 1.5, 0,-3,
                        -3, 0.5, 1, 1.5, 1.5, 1, 0.5,-3,
                        -4,-2, 0, 0.5, 0.5, 0,-2,-4,
                        -5,-4,-3,-3,-3,-3,-4,-5]
    
    bishop_positions = [-2,-1,-1,-1,-1,-1,-1,-2,
                    -1, 0, 0, 0, 0, 0, 0,-1,
                    -1, 0, 0.5, 1, 1, 0.5, 0,-1,
                    -1, 0.5, 0.5, 1, 1, 0.5, 0.5,-1,
                    -1, 0, 1, 1, 1, 1, 0,-1,
                    -1, 1, 1, 1, 1, 1, 0,-1,
                    -1, 0.5, 0, 0, 0, 0, 0.5,-1,
                    -2,-1,-1,-1,-1,-1,-1,-2]

    rook_positions = [ 0, 0, 0, 0, 0, 0, 0, 0,
                    0.5, 1, 1, 1, 1, 1, 1, 0.5,
                    -0.5, 0, 0, 0, 0, 0, 0, -0.5,
                    -0.5, 0, 0, 0, 0, 0, 0, -0.5,
                    -0.5, 0, 0, 0, 0, 0, 0, -0.5,
                    -0.5, 0, 0, 0, 0, 0, 0, -0.5,
                    -0.5, 0, 0, 0, 0, 0, 0, -0.5,
                    0, 0, 0, 0.5, 0.5, 0, 0, 0]

    queen_positions = [-2,-1,-1,-0.5,-0.5,-1,-1,-2,
                    -1, 0, 0, 0, 0, 0, 0,-1,
                    -1, 0, 0.5, 0.5, 0.5, 0.5, 0,-1,
                    -0.5, 0, 0.5, 0.5, 0.5, 0.5, 0, -0.5,
                    0, 0, 0.5, 0.5, 0.5, 0.5, 0,-0.5,
                    -1, 0.5, 0.5, 0.5, 0.5, 0.5, 0,-1,
                    -1, 0, 0.5, 0, 0, 0, 0,-1,
                    -2,-1,-1,-0.5,-0.5,-1,-1,-2]

    king_positions = [-3,-4,-4,-5,-5,-4,-4,-3,
                    -3,-4,-4,-5,-5,-4,-4,-3,
                    -3,-4,-4,-5,-5,-4,-4,-3,
                    -3,-4,-4,-5,-5,-4,-4,-3,
                    -2,-3,-3,-4,-4,-3,-3,-2,
                    -1,-2,-2,-2,-2,-2,-2,-1,
                    2, 2, 0, 0, 0, 0, 2, 2,
                    2, 3, 1, 0, 0, 1, 3, 2]

    evaluation = 0
    for square in chess.SQUARES:
        piece = board.piece_at(square)
        if piece is not None:
            # Valor base da peca
            if piece.piece_type == chess.PAWN:
                evaluation += 1 + pawn_positions[square] if piece.color == chess.WHITE else -1 - pawn_positions[square]
            elif piece.piece_type == chess.KNIGHT:
                evaluation += 3 + knight_positions[square] if piece.color == chess.WHITE else -3 - knight_positions[square]
            elif piece.piece_type == chess.BISHOP:
                evaluation += 3 + bishop_positions[square] if piece.color == chess.WHITE else -3 - bishop_positions[square]
            elif piece.piece_type == chess.ROOK:
                evaluation += 5 + rook_positions[square] if piece.color == chess.WHITE else -5 - rook_positions[square]
            elif piece.piece_type == chess.QUEEN:
                evaluation += 9 + queen_positions[square] if piece.color == chess.WHITE else -9 - queen_positions[square]
            elif piece.piece_type == chess.KING:
                evaluation += king_positions[square] if piece.color == chess.WHITE else -king_positions[square]

    # Avalia movimentos legais
    evaluation += 0.1 * len(list(board.legal_moves))

    return evaluation

transposition_table = {}

def alphabeta(board, depth, alpha, beta, maximizing_player):
    # Se a posicao atual estiver na tabela de transposicao, retorne o valor armazenado
    fen_key = board.fen()
    if fen_key in transposition_table:
        return transposition_table[fen_key]

    if depth == 0 or board.is_game_over():
        value = evaluate_board(board)
        transposition_table[fen_key] = value
        return value

    if maximizing_player:
        max_eval = float('-inf')
        for move in board.legal_moves:
            board.push(move)
            eval = alphabeta(board, depth-1, alpha, beta, False)
            board.pop()
            max_eval = max(max_eval, eval)
            alpha = max(alpha, eval)
            if beta <= alpha:
                break
        transposition_table[fen_key] = max_eval
        return max_eval
    else:
        min_eval = float('inf')
        for move in board.legal_moves:
            board.push(move)
            eval = alphabeta(board, depth-1, alpha, beta, True)
            board.pop()
            min_eval = min(min_eval, eval)
            beta = min(beta, eval)
            if beta <= alpha:
                break
        transposition_table[fen_key] = min_eval
        return min_eval

def best_move(board, depth):
    best_move = None
    best_value = float('-inf') if board.turn == chess.WHITE else float('inf')
    for move in board.legal_moves:
        board.push(move)
        board_value = alphabeta(board, depth-1, float('-inf'), float('inf'), board.turn == chess.BLACK)
        board.pop()
        if board.turn == chess.WHITE and board_value > best_value:
            best_value = board_value
            best_move = move
        elif board.turn == chess.BLACK and board_value < best_value:
            best_value = board_value
            best_move = move
    return best_move

def run_best_move(result, board, depth):
    result.append(best_move(board, depth))

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(100, 100, 690, 690)

        self.widgetSvg = QSvgWidget(parent=self)
        self.widgetSvg.setGeometry(0, 0, 690, 690)

        self.user_color = None
        while self.user_color not in ['w', 'b']:
            self.user_color = input("Você quer jogar com as Brancas (w) ou Pretas (b)? ").lower()
        self.user_plays_white = self.user_color == 'w'

        self.chessboard = chess.Board()
        self.selected_square = None
        self.last_move = None

        if not self.user_plays_white:
            result = []
            depth = 3 # PROFUNDIDADE DO ALGORITMO ALPHABETA
            thread = threading.Thread(target=run_best_move, args=(result, self.chessboard, depth))
            thread.start()
            thread.join(timeout=240)  # Limite de 4 minutos

            if thread.is_alive():
                print("IA demorou demais! Você ganhou!")
                exit()

            move = result[0] if result else None
            if move:
                self.chessboard.push(move)
                print(f"IA jogou: {move.uci()}")
                self.last_move = move
                self.clear_highlight()
                self.widgetSvg.load(self.get_svg())
                self.selected_square = None

        self.widgetSvg.load(self.get_svg())

    def get_svg(self):
        return chess.svg.board(self.chessboard, lastmove=self.last_move).encode("UTF-8")

    def highlight_squares(self, squares):
        self.chessboard_svg = chess.svg.board(self.chessboard, squares=squares, lastmove=self.last_move)
        self.widgetSvg.load(self.chessboard_svg.encode("UTF-8"))

    def clear_highlight(self):
        self.widgetSvg.load(self.get_svg())

    def mousePressEvent(self, event):
        if event.button() == 1:
            x, y = event.x(), event.y()
            square_width = self.widgetSvg.width() // 8
            square_height = self.widgetSvg.height() // 8
            file = x // square_width
            rank = 7 - y // square_height
            square = chess.square(file, rank)

            if self.selected_square is None:
                if self.chessboard.piece_at(square) and self.user_plays_white == self.chessboard.turn:
                    self.selected_square = square
                    self.highlight_squares([square])
                    moves = self.chessboard.legal_moves
                    self.highlight_squares([move.to_square for move in moves if move.from_square == square])

            else:
                move = chess.Move(self.selected_square, square)

                if move in self.chessboard.legal_moves:
                    self.chessboard.push(move)
                    self.last_move = move
                    self.clear_highlight()
                    self.widgetSvg.load(self.get_svg())
                self.selected_square = None

                if not self.user_plays_white == self.chessboard.turn:
                    result = []
                    depth = 3 # PROFUNDIDADE DO ALGORITMO ALPHABETA
                    thread = threading.Thread(target=run_best_move, args=(result, self.chessboard, depth))
                    thread.start()
                    thread.join(timeout=240)  # Limite de 4 minutos

                    if thread.is_alive():
                        print("IA demorou demais! Você ganhou!")
                        exit()

                    move = result[0] if result else None
                    if move:
                        self.chessboard.push(move)
                        print(f"IA jogou: {move.uci()}")
                        self.last_move = move
                        self.clear_highlight()
                        self.widgetSvg.load(self.get_svg())
                        self.selected_square = None

                    else:
                        print("Nenhum movimento valido encontrado para a IA!")
                        exit

if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()
    if window.chessboard.is_game_over():
        if window.chessboard.is_checkmate():
            if not window.chessboard.turn:
                print("Cheque-Mate! Vitória das brancas!")
            else:
                print("Cheque-Mate! Vitória das pretas!")
        elif window.chessboard.is_stalemate():
            print("Empate (Rei afogado)")
        else:
            print("Declarado empate")

        