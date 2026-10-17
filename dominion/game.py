from random import Random


def starting_deck() -> list[str]:
    raise NotImplementedError


def draw_cards(
    deck: list[str], discard: list[str], hand: list[str], count: int, rng: Random
) -> None:
    raise NotImplementedError


def score_cards(cards: list[str]) -> int:
    raise NotImplementedError
