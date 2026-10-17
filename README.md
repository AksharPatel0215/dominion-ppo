# Dominion PPO

PPO implemented from scratch with PyTorch to learn Dominion.
Planned website: play against agents and watch simulations.

## Scope

Two players, base-game rules, fixed Kingdom, no expansions.
Planned Kingdom: Village, Smithy, Market, Festival, Laboratory, Council Room,
Chapel, Workshop, Moneylender, Gardens. Effects will be added in stages.
Game logic, PPO, and website are not implemented yet.

## First checkpoint

Python 3.10+. No third-party dependencies required yet.

```sh
python3 -m unittest discover -s tests -v
```

Tests intentionally fail until the placeholders are implemented.
First implement starting decks, drawing and reshuffling, and basic scoring.

## Roadmap

1. Deck operations and card definitions.
2. Turn phases, supply, card effects, and game termination.
3. Baselines and observations that respect hidden information.
4. Networks, rollouts, advantages, and clipped PPO.
5. Evaluation across random seeds and opponents.
6. Interactive website and training comparisons.

Official rules: https://www.riograndegames.com/wp-content/uploads/2016/09/Dominion2E.pdf

Author-written implementation with guided explanations and scaffolding assistance.
