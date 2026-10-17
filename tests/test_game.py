from collections import Counter
from random import Random
import unittest

from dominion.game import starting_deck, draw_cards, score_cards


class StartingDeckTests(unittest.TestCase):
    def test_composition(self):
        self.assertEqual(Counter(starting_deck()), {"copper": 7, "estate": 3})

    def test_independence(self):
        first, second = starting_deck(), starting_deck()
        first.clear()
        self.assertEqual(len(second), 10)


class DrawTests(unittest.TestCase):
    def test_draw_from_end(self):
        deck, discard, hand = ["copper", "estate"], [], []
        draw_cards(deck, discard, hand, 1, Random(0))
        self.assertEqual(deck, ["copper"])
        self.assertEqual(hand, ["estate"])

    def test_reshuffle_and_exhaust(self):
        deck, discard, hand = ["gold"], ["estate", "copper"], []
        draw_cards(deck, discard, hand, 5, Random(0))
        self.assertEqual(hand[0], "gold")
        self.assertCountEqual(hand, ["gold", "estate", "copper"])
        self.assertEqual((deck, discard), ([], []))

    def test_zero_draw(self):
        deck, discard, hand = [], ["estate"], ["copper"]
        draw_cards(deck, discard, hand, 0, Random(0))
        self.assertEqual((deck, discard, hand), ([], ["estate"], ["copper"]))


class ScoreTests(unittest.TestCase):
    def test_base_cards(self):
        self.assertEqual(score_cards(["estate", "duchy", "province", "curse", "gold"]), 9)

    def test_empty(self):
        self.assertEqual(score_cards([]), 0)


if __name__ == "__main__":
    unittest.main()
