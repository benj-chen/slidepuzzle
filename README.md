# Slidepuzzle
I'm Benjamin Chen, author of this slidepuzzle, a 1-player game in which the object is to arrange the tiles in order from 1 to 15. Libraries used: random

## Gameplay

To run the game, **it is important to note that running the file in the terminal will produce many errors.** It must be run in a python interpreter like IDLE, or on the command line built into some Python interpreters.

Here's an example of gameplay:
```
|----|----|----|----|
| 01 | 10 | 02 | 15 |
|----|----|----|----|
| 06 | 09 |    | 14 |
|----|----|----|----|
| 03 | 04 | 13 | 11 |
|----|----|----|----|
| 12 | 05 | 07 | 08 |
|----|----|----|----|
Move: 09
|----|----|----|----|
| 01 | 10 | 02 | 15 |
|----|----|----|----|
| 06 |    | 09 | 14 |
|----|----|----|----|
| 03 | 04 | 13 | 11 |
|----|----|----|----|
| 12 | 05 | 07 | 08 |
|----|----|----|----|
Move: 10
|----|----|----|----|
| 01 |    | 02 | 15 |
|----|----|----|----|
| 06 | 10 | 09 | 14 |
|----|----|----|----|
| 03 | 04 | 13 | 11 |
|----|----|----|----|
| 12 | 05 | 07 | 08 |
|----|----|----|----|
Move: 02
|----|----|----|----|
| 01 | 02 |    | 15 |
|----|----|----|----|
| 06 | 10 | 09 | 14 |
|----|----|----|----|
| 03 | 04 | 13 | 11 |
|----|----|----|----|
| 12 | 05 | 07 | 08 |
|----|----|----|----|
Move: 09
|----|----|----|----|
| 01 | 02 | 09 | 15 |
|----|----|----|----|
| 06 | 10 |    | 14 |
|----|----|----|----|
| 03 | 04 | 13 | 11 |
|----|----|----|----|
| 12 | 05 | 07 | 08 |
|----|----|----|----|
Move: 13
|----|----|----|----|
| 01 | 02 | 09 | 15 |
|----|----|----|----|
| 06 | 10 | 13 | 14 |
|----|----|----|----|
| 03 | 04 |    | 11 |
|----|----|----|----|
| 12 | 05 | 07 | 08 |
|----|----|----|----|
Move: 04
|----|----|----|----|
| 01 | 02 | 09 | 15 |
|----|----|----|----|
| 06 | 10 | 13 | 14 |
|----|----|----|----|
| 03 |    | 04 | 11 |
|----|----|----|----|
| 12 | 05 | 07 | 08 |
|----|----|----|----|
Move: 
```
As shown, the player can enter a number that is above, below, to the left of, or to the right of the current place of the empty space, which simulates a real slidepuzzle by sliding the chosen number in the direction of the empty space, switching the two tiles.

## Shuffling The Board

Because there are sometimes cases when solving the puzzle is impossible, rather than using random.shuffle(), the computer shuffles the "tiles" similarly to how a human would in real life, by switching the empty space with one that is above, to the left of, to the right of, or below it, depending on the position of the space (obviously, moving to the left if you're on the left edge is impossible). The program chooses which way to shuffle the empty space using random.choice(), and then repeats it 10000 times. This guarantees a solvable scramble every time someone plays the game.
