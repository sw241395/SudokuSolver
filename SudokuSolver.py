import sys
import tkinter
import Solver
import os


# Get arguments to run command line
arguments = sys.argv[1:len(sys.argv)]
count = 0
csv_file_path = None
height = None
width = None
for arg in arguments:
    if arg == '-h':
        height = arguments[count + 1]
    elif arg == '-w':
        width = arguments[count + 1]
    elif arg == '--help':
        print('Some help message')
        quit()
    elif os.path.isfile(arg):
        # check file is csv
        csv_file_path = arg
        if csv_file_path[-4:] != '.csv':
            print('Some message about valid file')
            quit()
    count += 1


# Run command line version of the solver
if csv_file_path is not None and height is None and width is None:
    print(Solver.solve_square_grid(csv_file_path))
    quit()
elif csv_file_path is not None and height.isdigit() and width.isdigit():
    print(Solver.solve_grid(csv_file_path, int(height), int(width)))
    quit()
elif len(arguments) > 0:
    print('Some help message')
    quit()


# TODO: Create GUI
