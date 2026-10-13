from app.game.board import Board
from app.game.piece import Piece

def test_board_initialization():
    board = Board(size=20)
    assert board.size == 20
    assert len(board.grid) == 0  # Plansza powinna być pusta na start

def test_place_piece_successfully():
    board = Board()
    piece = Piece("LINE3", [(0, 0), (1, 0), (2, 0)])
    
    # Próbujemy położyć klocek zaczynając od x=0, y=0 dla Gracza 1
    success = board.place_piece(piece, 0, 0, "player_1")
    
    assert success is True
    assert board.grid[(0, 0)] == "player_1"
    assert board.grid[(1, 0)] == "player_1"
    assert board.grid[(2, 0)] == "player_1"

def test_place_piece_out_of_bounds():
    board = Board()
    piece = Piece("LINE3", [(0, 0), (1, 0), (2, 0)])
    
    # Próbujemy położyć klocek za blisko prawej krawędzi (wyjdzie poza 20)
    success = board.place_piece(piece, 19, 0, "player_1")
    
    assert success is False
    assert len(board.grid) == 0  # Plansza musi pozostać pusta

def test_place_piece_on_occupied_squares():
    board = Board()
    piece1 = Piece("DOT", [(0, 0)])
    piece2 = Piece("LINE3", [(0, 0), (1, 0), (2, 0)])
    
    # Pierwszy klocek zajmuje pole (5, 5)
    board.place_piece(piece1, 5, 5, "player_1")
    
    # Drugi klocek próbuje wejść na zajęte pole (zaczyna na 4, 5, więc pola to: 4,5; 5,5; 6,5)
    success = board.place_piece(piece2, 4, 5, "player_2")
    
    assert success is False
    # Pole 5,5 nadal należy do gracza 1
    assert board.grid[(5, 5)] == "player_1"