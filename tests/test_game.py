"""Behavioral checks for checkpoint 1; no third-party test runner required."""

from copy import deepcopy
import unittest

from reversi.game import get_flips, initial_board, legal_moves


class InitialBoardTests(unittest.TestCase):
    def test_starting_position(self):
        board = initial_board()
        self.assertEqual(len(board), 8)
        self.assertTrue(all(len(row) == 8 for row in board))
        occupied = {(r, c): board[r][c] for r in range(8)
                    for c in range(8) if board[r][c] != 0}
        self.assertEqual(occupied, {(3, 3): -1, (4, 4): -1,
                                    (3, 4): 1, (4, 3): 1})

    def test_rows_and_games_are_independent(self):
        first, second = initial_board(), initial_board()
        first[0][0] = 1
        self.assertEqual(first[1][0], 0)
        self.assertEqual(second[0][0], 0)


class CaptureTests(unittest.TestCase):
    def test_capture_in_each_direction_and_for_each_color(self):
        for player in (1, -1):
            for dr, dc in ((-1, -1), (-1, 0), (-1, 1), (0, -1),
                           (0, 1), (1, -1), (1, 0), (1, 1)):
                with self.subTest(player=player, direction=(dr, dc)):
                    board = [[0] * 8 for _ in range(8)]
                    board[3 + dr][3 + dc] = -player
                    board[3 + 2 * dr][3 + 2 * dc] = player
                    before = deepcopy(board)
                    self.assertEqual(get_flips(board, player, 3, 3),
                                     [(3 + dr, 3 + dc)])
                    self.assertEqual(board, before)

    def test_capture_multiple_rays_and_multiple_discs(self):
        board = [[0] * 8 for _ in range(8)]
        board[3][4:7] = [-1, -1, 1]
        board[4][3], board[5][3] = -1, 1
        self.assertCountEqual(get_flips(board, 1, 3, 3),
                              [(3, 4), (3, 5), (4, 3)])

    def test_invalid_targets_and_unclosed_lines(self):
        board = [[0] * 8 for _ in range(8)]
        board[0][1], board[0][3] = -1, 1  # Empty gap breaks capture.
        board[1][0] = 1  # Friendly neighbor captures nothing.
        board[7][6], board[7][7] = -1, -1  # Edge breaks capture.
        for row, col in ((0, 0), (7, 5), (0, 3), (-1, 0), (8, 0)):
            with self.subTest(target=(row, col)):
                self.assertEqual(get_flips(board, 1, row, col), [])


class LegalMovesTests(unittest.TestCase):
    def test_starting_moves_for_both_players(self):
        board = initial_board()
        before = deepcopy(board)
        self.assertEqual(legal_moves(board, 1),
                         [(2, 3), (3, 2), (4, 5), (5, 4)])
        self.assertEqual(legal_moves(board, -1),
                         [(2, 4), (3, 5), (4, 2), (5, 3)])
        self.assertEqual(board, before)

    def test_no_moves_on_full_board(self):
        board = [[1] * 8 for _ in range(8)]
        self.assertEqual(legal_moves(board, 1), [])
        self.assertEqual(legal_moves(board, -1), [])


if __name__ == "__main__":
    unittest.main()
