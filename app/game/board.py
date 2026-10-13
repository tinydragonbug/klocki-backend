from typing import Dict, Tuple, List
from app.game.piece import Piece

class Board:
    def __init__(self, size: int = 20):
        # Rozmiar planszy (20x20)
        self.size = size
        # Słownik zajętych pól. Klucz to (x, y), wartość to ID gracza (np. "player_1")
        self.grid: Dict[Tuple[int, int], str] = {}

    def is_within_bounds(self, squares: List[Tuple[int, int]]) -> bool:
        """Sprawdza, czy wszystkie pola mieszczą się na planszy 20x20."""
        for x, y in squares:
            if x < 0 or x >= self.size or y < 0 or y >= self.size:
                return False
        return True

    def are_squares_free(self, squares: List[Tuple[int, int]]) -> bool:
        """Sprawdza, czy żadne z podanych pól nie jest już zajęte."""
        for sq in squares:
            if sq in self.grid:
                return False
        return True

    def place_piece(self, piece: Piece, board_x: int, board_y: int, player_id: str) -> bool:
        """
        Próbuje położyć klocek na planszy. 
        Zwraca True, jeśli się udało. Zwraca False, jeśli ruch jest nielegalny.
        """
        target_squares = piece.get_squares_at(board_x, board_y)

        # 1. Sprawdź granice planszy
        if not self.is_within_bounds(target_squares):
            return False

        # 2. Sprawdź, czy pola są wolne
        if not self.are_squares_free(target_squares):
            return False

        # Jeśli wszystko jest OK, zapisz pola w słowniku na stałe
        for sq in target_squares:
            self.grid[sq] = player_id
            
        return True