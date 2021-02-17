import numpy
import pandas


# function to check a cell in a grid
def check_cell(grid_as_row, cell, size, boxes):
    # Code to check columns
    column = cell % size
    while column <= (size**2) - 1:
        if column != cell and grid_as_row[cell] == grid_as_row[column]:
            return False
        column += size

    # Code to check rows
    row = cell - (cell % size)
    for y in range(row, row + size - 1, 1):
        if y != cell and grid_as_row[y] == grid_as_row[cell]:
            return False

    for box in boxes:
        if cell in box:
            for z in box:
                if cell != z and grid_as_row[cell] == grid_as_row[z]:
                    return False
    return True


# function to check the whole sudoku grid
def check_grid(grid, size, boxes):
    for x in range(size**2):
        if not check_cell(grid, x, size, boxes):
            return False
    return True


# function to take CSV file and convert it too a grid
def read_csv(path_to_csv):
    grid = pandas.read_csv(path_to_csv, header=None)
    grid.fillna(0, inplace=True)
    return grid.to_numpy()


# Solve the grid (non square)
def solve_grid(path, box_height, box_width):
    # get CSV
    grid = pandas.read_csv(path, header=None)
    grid.fillna(0, inplace=True)
    grid.to_numpy()

    size = len(grid)

    # check if the height and width can be used
    if box_height*box_width != size:
        print('Some message about height and width not correct')
        quit()

    # TODO: add initial check to see if solvable

    # Do to solving
    solution = solving_algorithm(grid, size, box_height, box_width)

    return solution


# Solve grid (square)
def solve_square_grid(path):
    # get CSV
    try:
        grid = pandas.read_csv(path, header=None)
        grid.fillna(0, inplace=True)
        grid.to_numpy().astype(numpy.int8)
    except:
        print('some message about the csv not being correct')
        quit()

    # Check length is square
    size = len(grid)
    if size**0.5 != int(size**0.5):
        print('some message about the csv not being square and need -h and -w inputs')
        quit()
    height_and_width = size**0.5

    # Do the solving
    solution = solving_algorithm(grid, size, height_and_width, height_and_width)

    return solution


# The actual code to do the solving of the code
def solving_algorithm(grid, size, height, width):
    size2 = size**2
    grid_as_row = grid.to_numpy().reshape(size2).astype(numpy.int8)

    # TODO: add initial check to see if solvable

    # setting the array of choices
    choices = numpy.arange(size2, dtype=object)
    for a in range(size2):
        if grid_as_row[a] != 0:
            choices[a] = [grid_as_row[a]]
        else:
            choices[a] = list(numpy.arange(1, size + 1, dtype=numpy.int8))

    # setting up the boxes (group the larger grid into the smaller grids)
    number_line = numpy.arange(size2).reshape((size, size))
    boxes = []
    for hbox in numpy.hsplit(number_line, height):
        for vbox in numpy.vsplit(hbox, width):
            boxes.append(vbox.reshape(size))

    # reduce the newly confirmed integers
    loop = True
    while loop:
        loop = False
        for e in range(size2):
            if len(choices[e]) == 1:
                # Code to remove the same ints from columns
                column = e % size
                while column <= size2 - 1:
                    if column != e and choices[e] in choices[column]:
                        choices[column].remove(choices[e])
                        loop = True
                    column += size

                # Code to remove the same ints from rows
                row = e - (e % size)
                for f in range(row, row + size - 1, 1):
                    if f != e and choices[e] in choices[f]:
                        choices[f].remove(choices[e])
                        loop = True

                # Code to remove the same ints from box
                for box in boxes:
                    if e in box:
                        for g in box:
                            if g != e and choices[e] in choices[g]:
                                choices[g].remove(choices[e])
                                loop = True

    # Back tracking
    cell = 0
    list_cell = 0
    grid_as_row_copy = grid_as_row
    try:
        while cell < size2:
            # set int
            grid_as_row_copy[cell] = choices[cell][list_cell]

            # check
            check = check_cell(grid_as_row_copy, cell, size, boxes)

            # if ok move to next cell
            if check:
                cell += 1
                list_cell = 0
            # if not then set int again
            elif list_cell < len(choices[cell]) - 1:
                list_cell += 1
            else:
                back_track = True
                while back_track:
                    # if no more ints then back track
                    grid_as_row_copy[cell] = 0
                    cell -= 1

                    if choices[cell].index(grid_as_row_copy[cell]) + 1 < len(choices[cell]):
                        list_cell = choices[cell].index(grid_as_row_copy[cell]) + 1
                        back_track = False

        # check the solution
        if check_grid(grid_as_row_copy, size, boxes):
            return numpy.asarray(grid_as_row_copy).reshape(size, size)
        else:
            return 'Could not be solved using back tracking'
    except:
        return 'Could not be solved using back tracking'

    # TODO: Implement brute force method if user wants
