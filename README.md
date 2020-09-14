# sudoku

The solution is base on constraint satisfaction problem from this book https://www.manning.com/books/classic-computer-science-problems-in-python I bought a year ago. The CSP chapter seems to be available for free at the monment https://freecontent.manning.com/constraint-satisfaction-problems-in-python/

I didn't do any optimization, so it just simple depth first search to brute force the constraints and its variables. T

The puzzles from input.txt took reasonable-ish time to solve.
puzzle 1:   steps - 53167    run time (second) - 0.2093372344970703
puzzle 2:   steps - 670393   run time (second) - 2.6448049545288086
puzzle 3:   steps - 305245   run time (second) - 1.213304042816162
puzzle 4:   steps - 6049228  run time (second) - 25.654021978378296
puzzle 5:   steps - 321750   run time (second) - 1.3364019393920898

However the one from evil.txt took 141 million steps and 9 minutes to solve:
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


What optimization can be done?
