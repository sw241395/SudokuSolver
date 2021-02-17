# SudokuSolver
First attempt at a python project and using git

Just a basic command line script to solve sudoku puzzles. Will work to solve any NxN sized puzzle. You will need to indicate the size of the sub-square if you are trying to solve a non-square number sized grid.

For example for a 10x10 grid if you will need to give the sub box size of hight 2 and width 5.

---

Requirements:
>Numpy, Pandas, 

---

How to run: 
'''
python3 SudokuSolver.py PathToCSV
'''

---

How it works:

1. Take the square as a form of CSV file
2. Convert it into an array
3. For each square there can be N number of values it can be. So create N^2 number of arrays where each entry is an array from 1 to N
4. As we already know some values in the square we can replace substitute them into the above array
5. Then we can reduce the number of values in each array by removing values if they are in the same row, column, or sub-box as a known value
6. We can loop this process as doing the above process could reveal other known values
7. So now we have an array for the values that could go into each square of the grid. 
8. Then start to back track but only use the values in th array for each individual square

---

TODO:
* Make a GUI using tkinter
* Implement a brute force method when back tracking does not work
* Code improvements to make it more efficient or cleaner
* Better print messages 
* Update this readme

