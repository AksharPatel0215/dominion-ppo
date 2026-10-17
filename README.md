# Reversi PPO

A learning project: implement standard 8x8 Reversi and PPO, then build an
interactive website for playing against trained agents and running simulations.

## Current status

Checkpoint 1: game-rule method placeholders. The game and PPO are not implemented.
The implementation is written by the project author, with guided explanations
and scaffolding assistance.

## Roadmap

1. Game engine and rule checks.
2. Random and scripted baseline opponents.
3. Policy/value networks and PPO implemented directly with PyTorch.
4. Reproducible evaluation and saved agent checkpoints.
5. Interactive website: play against an agent or watch simulations.
6. Training efficiency and presentation improvements.

## First checkpoint

Use Python 3.10 or newer. No third-party packages are needed yet.
Run commands from this project directory.

```sh
python3 -m unittest discover -s tests -v
```

The checks intentionally report errors until the placeholders in
`reversi/game.py` are implemented. Implement in order:

1. `initial_board`: construct the starting board with independent rows.
2. `get_flips`: identify captures in all eight directions without mutation.
3. `legal_moves`: enumerate placements that capture at least one disc.

Board cells use `0` for empty, `1` for black, and `-1` for white.
Coordinates are zero-based `(row, column)`. White starts at `(3, 3)` and
`(4, 4)`; black starts at `(3, 4)` and `(4, 3)`. Black moves first.

The game engine will remain separate from training and display code so it can
serve both training and the future website. PyTorch will be introduced when we
reach neural networks; no prebuilt PPO implementation will be used.
