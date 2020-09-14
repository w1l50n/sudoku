# sudoku

The solution is base on constraint satisfaction problem from this book https://www.manning.com/books/classic-computer-science-problems-in-python I bought a year ago. The CSP chapter seems to be available for free at the monment https://freecontent.manning.com/constraint-satisfaction-problems-in-python/

I didn't do any optimization, so it just simple depth first search to brute force the constraints and its variables.
  
To run the solver (python3 require): `python sudokus.py inputs.txt`

Each line in the input file represent one sudoku puzzle ("." is unfilled space) 
```
.4..6.5...........57......3.......8......924....2.6....9...3...6.871.4..13..4.7.5
...4...6.6.3...1...8.....7........2.....5.49...269...5..4..3...296.....33.5..1..8
.9..16...6......2..4..5....7...39.5.....4.......7...86..1.............9..37...468
2..9.........2.3......5...7..8...2....1..46.......5.1.5...1....6.7..8..1.4.7....9
...15..6.3......71.6...3.....927..........4..67.....5....4.2..6.45...9.3...8.....
``` 

The steps and time need to solve the puzzles from inputs.txt:
```
puzzle 1:   steps - 53167    run time (second) - 0.2093372344970703
puzzle 2:   steps - 670393   run time (second) - 2.6448049545288086
puzzle 3:   steps - 305245   run time (second) - 1.213304042816162
puzzle 4:   steps - 6049228  run time (second) - 25.654021978378296
puzzle 5:   steps - 321750   run time (second) - 1.3364019393920898
```

However, the one from evil.txt took 141 million steps and 9 minutes to solve:
```
$ python sudokus.py evil.txt
puzzle:

| - - - - - -  |  - - - - - -  |  - - - - - -  |

| 4    *    *  |  *    *    *  |  8    *    5  |

| *    3    *  |  *    *    *  |  *    *    *  |

| *    *    *  |  7    *    *  |  *    *    *  |

| - - - - - -  |  - - - - - -  |  - - - - - -  |

| *    2    *  |  *    *    *  |  *    6    *  |

| *    *    *  |  *    8    *  |  4    *    *  |

| *    *    *  |  *    1    *  |  *    *    *  |

| - - - - - -  |  - - - - - -  |  - - - - - -  |

| *    *    *  |  6    *    3  |  *    7    *  |

| 5    *    *  |  2    *    *  |  *    *    *  |

| 1    *    4  |  *    *    *  |  *    *    *  |

| - - - - - -  |  - - - - - -  |  - - - - - -  |

solution (141734162 steps, 545.640115737915 seconds):

| - - - - - -  |  - - - - - -  |  - - - - - -  |

| 4    1    7  |  3    6    9  |  8    2    5  |

| 6    3    2  |  1    5    8  |  9    4    7  |

| 9    5    8  |  7    2    4  |  3    1    6  |

| - - - - - -  |  - - - - - -  |  - - - - - -  |

| 8    2    5  |  4    3    7  |  1    6    9  |

| 7    9    1  |  5    8    6  |  4    3    2  |

| 3    4    6  |  9    1    2  |  7    5    8  |

| - - - - - -  |  - - - - - -  |  - - - - - -  |

| 2    8    9  |  6    4    3  |  5    7    1  |

| 5    7    3  |  2    9    1  |  6    8    4  |

| 1    6    4  |  8    7    5  |  2    9    3  |

| - - - - - -  |  - - - - - -  |  - - - - - -  |

```
What optimization can be done? ( •̀ᴗ•́ )و ̑̑