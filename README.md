# Soduko Solver
This implementation is my solution to the third obligatory assignment in INF-1400: Objektorientert Programmering. It solves soduko boards which can be found in the csv files. The rule in sudoku is that every row/box/coloumn has the numbers 1-9


### Authors
Tora K. Homme


## Running the solver
Go to the src directory

```bash
  cd SudokuSolver/src
```
Run the program
```bash
  python3 sudokuboard.py
```

## Changing number of prints/boards
- Go to the sudokuboard.py file
- At line #185 you can change the source file to either
    - "sudoku_10.csv"
    - "sudoku_100.csv"
    - "sudoku_1M.csv"
  which are respectivly 10, 100 and 1 million boards
- At line #188 you have to change the condition based on how many boards you want it to solve. Recomended 10, 100 or 1 000 000 based on the number of boards in the file.
- At line #195 you can change the conditions for which boards to print.
- At line #198 there is a print statement which prints every solved boards number. If you have 1 M boards, this might be excessive, and you might want to comment it out.

