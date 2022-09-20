# nqueenplay

```py
    1   2   3   4   5   6   7   8 
  ---------------------------------
8 |   |   | Q |   |   |   |   |   | 8
  ---------------------------------
7 |   |   |   |   | Q |   |   |   | 7
  ---------------------------------
6 |   |   |   |   |   |   |   | Q | 6
  ---------------------------------
5 |   |   |   | Q |   |   |   |   | 5
  ---------------------------------
4 | Q |   |   |   |   |   |   |   | 4
  ---------------------------------
3 |   |   |   |   |   |   | Q |   | 3
  ---------------------------------
2 |   | Q |   |   |   |   |   |   | 2
  ---------------------------------
1 |   |   |   |   |   | Q |   |   | 1
  ---------------------------------
    1   2   3   4   5   6   7   8 
```

`nqueenplay` is N-Queens puzzle player. This tool will generate randomly or randomly locked puzzle, you may use this as "a boxing bag" to practice problem solving algorithm.

![GitHub](https://img.shields.io/github/license/eiproject/nqueenplay)
![GitHub repo size](https://img.shields.io/github/repo-size/eiproject/nqueenplay)
![GitHub contributors](https://img.shields.io/github/contributors/eiproject/nqueenplay)

## Installation

This python package available on pip installation using

`pip install nqueenplay`

## Requirements

Available on Python 3

## Documentation

A to Z explanations to use this tool

### Generate Random Puzzle

To generate a random puzzle you can do:

```py
N = 4 # any integer
nqueens = NQueen(N)
```

or

```py
N = 4 # any integer
nqueens = NQueen(n=N, number_lock=0) # 0 = no lock
```

### Generate Random Locked Puzzle

Random locked mean the distribution of queen is randomize, and there is locking mechanism to make sure the queen position won't change for another run. To generate a random locked puzzle you can do:

```py
N = 4 # any integer
lock = 1 # any integer
nqueens = NQueen(n=N, number_lock=lock)
```

### Get Number of Queens

To get number of queen:

```py
N = 4
nqueens = NQueen(n=N, number_lock=1)
number_of_queen = nqueens.get_number_of_queens()
```

Output:

```py
print(number_of_queen)
# 4
```

### Get Queens Position

To get queen position:

```py
N = 4
nqueens = NQueen(n=N, number_lock=1)
positions = nqueens.get_queen_positions()
```

Output:

```py
print(positions)
# [(1, 1), (2, 4), (3, 3), (4, 2)]
```

Each tuple is The Queen coordinate, there is 4 attack pairs

### Check Number of Attack Pairs

To check how many attack pairs in the current board:

```py
N = 4
nqueens = NQueen(n=N, number_lock=1)
pairs = nqueens.get_attack_pairs()
```

Output:

```py
print(pairs) 
# [[(1, 1), (3, 3)], [(2, 4), (3, 3)], [(2, 4), (4, 2)], [(3, 3), (4, 2)]]
```

Each tuple is The Queen coordinate, there is 4 attack pairs

### Show The Board

To show the current board:

```py
N = 4
nqueens = NQueen(n=N, number_lock=1)
nqueens.show()
```

output:

```py
    1   2   3   4 
  -----------------
4 |   | Q |   |   | 4
  -----------------
3 |   |   | Q |   | 3
  -----------------
2 |   |   |   | Q | 2
  -----------------
1 | Q |   |   |   | 1
  -----------------
    1   2   3   4 
```

### Show The Attack Pairs

To show the current board attack pairs:

```py
N = 4
nqueens = NQueen(n=N, number_lock=1)
nqueens.show_attacking_pairs()
```

output

```py
# attack_pairs [(1, 3), (2, 3), (2, 4), (3, 4)]
# Number of attacking pair(s): 4
```

### Move The Queen

Queen is column locked, so you can only move one queen to a different row

#### Move the queen upside

Move Queen to upside with specific range:

```py
N = 4
nqueens = NQueen(n=N, number_lock=1)
nqueens.show()
nqueens.move_up(queens_index=1, movement_length=2)
nqueens.show()
```

output:

```py
    1   2   3   4 
  -----------------
4 |   | Q |   |   | 4
  -----------------
3 |   |   | Q |   | 3
  -----------------
2 |   |   |   | Q | 2
  -----------------
1 | Q |   |   |   | 1
  -----------------
    1   2   3   4 
    1   2   3   4 
  -----------------
4 |   | Q |   |   | 4
  -----------------
3 | Q |   | Q |   | 3
  -----------------
2 |   |   |   | Q | 2
  -----------------
1 |   |   |   |   | 1
  -----------------
    1   2   3   4 
```

#### Move the queen downside

Move Queen to downside with specific range:

```py
N = 4
nqueens = NQueen(n=N, number_lock=1)
nqueens.show()
nqueens.move_down(queens_index=2, movement_length=2)
nqueens.show()
```

output:

```py
    1   2   3   4 
  -----------------
4 |   | Q |   |   | 4
  -----------------
3 |   |   | Q |   | 3
  -----------------
2 |   |   |   | Q | 2
  -----------------
1 | Q |   |   |   | 1
  -----------------
    1   2   3   4 
    1   2   3   4 
  -----------------
4 |   |   |   |   | 4
  -----------------
3 |   |   | Q |   | 3
  -----------------
2 |   | Q |   | Q | 2
  -----------------
1 | Q |   |   |   | 1
  -----------------
    1   2   3   4 
```

#### Move the queen to a random placement

Move Queen to random place in the column:

```py
N = 4
nqueens = NQueen(n=N, number_lock=1)
nqueens.show()
nqueens.move_random(queens_index=3)
nqueens.show()
```

output:

```py
    1   2   3   4 
  -----------------
4 |   | Q |   |   | 4
  -----------------
3 |   |   | Q |   | 3
  -----------------
2 |   |   |   | Q | 2
  -----------------
1 | Q |   |   |   | 1
  -----------------
    1   2   3   4 
    1   2   3   4 
  -----------------
4 |   | Q |   |   | 4
  -----------------
3 |   |   |   |   | 3
  -----------------
2 |   |   | Q | Q | 2
  -----------------
1 | Q |   |   |   | 1
  -----------------
    1   2   3   4 
```

## Copyright

Free to use! Under MIT License.
