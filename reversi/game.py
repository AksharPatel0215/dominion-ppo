"""Pure game rules: no training or display dependencies.

Coordinates are zero-based (row, column), starting at the top left.
Cells: 0 = empty, 1 = black, -1 = white. Black moves first.
Functions return fresh results and must not mutate input boards.
"""


def initial_board() -> list[list[int]]:
    """Return a fresh 8x8 board as eight independent row lists.

    Place white at (3, 3) and (4, 4), black at (3, 4) and (4, 3).
    All other cells are empty. Separate calls must share no mutable rows.
    """
    raise NotImplementedError


def get_flips(
    board: list[list[int]], player: int, row: int, col: int
) -> list[tuple[int, int]]:
    """Return coordinates of opponent discs captured by a placement.

    Inputs: a valid 8x8 board, player in {1, -1}, and a target coordinate.
    Return [] if the target is outside the board, occupied, or captures nothing.
    Scan all eight directions. A capture needs one or more opponent discs
    followed immediately by a friendly disc, with no empty cells between.
    Exclude the placement square itself; result order does not matter.
    Do not place a disc, flip discs, or otherwise modify the board.
    """
    raise NotImplementedError


def legal_moves(
    board: list[list[int]], player: int
) -> list[tuple[int, int]]:
    """Return legal placement coordinates, sorted by row then column.

    Inputs: a valid 8x8 board and player in {1, -1}.
    A placement is legal exactly when get_flips returns a nonempty list.
    Return [] when the player has no legal placements. Passing is handled
    by the turn-management code we will introduce in a later checkpoint.
    Do not modify the board.
    """
    raise NotImplementedError
