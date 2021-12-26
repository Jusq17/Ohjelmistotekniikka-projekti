
sudoku_file = open("sudoku_grids.txt", "r")

lines = sudoku_file.readlines()

sudoku_grid =      [[0,0,0,0,0,0,0,0,0], 
                    [0,0,0,0,0,0,0,0,0], 
                    [0,0,0,0,0,0,0,0,0], 
                    [0,0,0,0,0,0,0,0,0], 
                    [0,0,0,0,0,0,0,0,0], 
                    [0,0,0,0,0,0,0,0,0], 
                    [0,0,0,0,0,0,0,0,0], 
                    [0,0,0,0,0,0,0,0,0], 
                    [0,0,0,0,0,0,0,0,0]]

def load_Level(level):

    print("In load level:")

    global sudoku_grid

    sudoku_grid =   [[],
                    [], 
                    [], 
                    [], 
                    [], 
                    [], 
                    [], 
                    [], 
                    []]    

    print(sudoku_grid)

    l = level                   
    i = 0
    c = 1

    for row in lines:

        if row == "n\n":

            c += 1
            continue

        if row != "\n" and c == l:

            for n in row:

                if n != "\n" and n != " " and n != "n\n":

                    if i < 9:
                    
                        sudoku_grid[i].append(int(n))

            i += 1

rows = [[(0,0), (0,1), (0,2), (0,3), (0,4), (0,5), (0,6), (0,7), (0,8)],
        [(1,0), (1,1), (1,2), (1,3), (1,4), (1,5), (1,6), (1,7), (1,8)],
        [(2,0), (2,1), (2,2), (2,3), (2,4), (2,5), (2,6), (2,7), (2,8)],
        [(3,0), (3,1), (3,2), (3,3), (3,4), (3,5), (3,6), (3,7), (3,8)],
        [(4,0), (4,1), (4,2), (4,3), (4,4), (4,5), (4,6), (4,7), (4,8)],
        [(5,0), (5,1), (5,2), (5,3), (5,4), (5,5), (5,6), (5,7), (5,8)],
        [(6,0), (6,1), (6,2), (6,3), (6,4), (6,5), (6,6), (6,7), (6,8)],
        [(7,0), (7,1), (7,2), (7,3), (7,4), (7,5), (7,6), (7,7), (7,8)],
        [(8,0), (8,1), (8,2), (8,3), (8,4), (8,5), (8,6), (8,7), (8,8)]]

cols = [[(0,0), (1,0), (2,0), (3,0), (4,0), (5,0), (6,0), (7,0), (8,0)],
        [(0,1), (1,1), (2,1), (3,1), (4,1), (5,1), (6,1), (7,1), (8,1)],
        [(0,2), (1,2), (2,2), (3,2), (4,2), (5,2), (6,2), (7,2), (8,2)],
        [(0,3), (1,3), (2,3), (3,3), (4,3), (5,3), (6,3), (7,3), (8,3)],
        [(0,4), (1,4), (2,4), (3,4), (4,4), (5,4), (6,4), (7,4), (8,4)],
        [(0,4), (1,5), (2,5), (3,5), (4,5), (5,5), (6,5), (7,5), (8,5)],
        [(0,6), (1,6), (2,6), (3,6), (4,6), (5,6), (6,6), (7,6), (8,6)],
        [(0,7), (1,7), (2,7), (3,7), (4,7), (5,7), (6,7), (7,7), (8,7)],
        [(0,8), (1,8), (2,8), (3,8), (4,8), (5,8), (6,8), (7,8), (8,8)]]

squares = [[(0,0), (0,1), (0,2), (1,0), (1,1), (1,2), (2,0), (2,1), (2,2)], 
            [(0,3), (0,4), (0,5), (1,3), (1,4), (1,5), (2,3), (2,4), (2,5)],
            [(0,6), (0,7), (0,8), (1,6), (1,7), (1,8), (2,6), (2,7), (2,8)],
            [(3,0), (3,1), (3,2), (4,0), (4,1), (4,2), (5,0), (5,1), (5,2)], 
            [(3,3), (3,4), (3,5), (4,3), (4,4), (4,5), (5,3), (5,4), (5,5)],
            [(3,6), (3,7), (3,8), (4,6), (4,7), (4,8), (5,6), (5,7), (5,8)],
            [(6,0), (6,1), (6,2), (7,0), (7,1), (7,2), (8,0), (8,1), (8,2)], 
            [(6,3), (6,4), (6,5), (7,3), (7,4), (7,5), (8,3), (8,4), (8,5)],
            [(6,6), (6,7), (6,8), (7,6), (7,7), (7,8), (8,6), (8,7), (8,8)]]

#Print matrix only for debugging purposes

def print_matrix():

    print("Matriisi:")

    for i in sudoku_grid:

        print(i)

def get_column(column_n):

    column = []

    for row in sudoku_grid:

        column.append(row[column_n])

    return column

def get_square(square_n):

    square = []

    if square_n == 1:

        for i in range(3):

            row = sudoku_grid[i]

            for j in range(3):

                square.append(row[j])

    if square_n == 2:

        for i in range(3):

            row = sudoku_grid[i]

            for j in range(3):

                square.append(row[j+3])

    if square_n == 3:

        for i in range(3):

            row = sudoku_grid[i]

            for j in range(3):

                square.append(row[j+6])

    if square_n == 4:

        for i in range(3):

            row = sudoku_grid[i+3]

            for j in range(3):

                square.append(row[j])

    if square_n == 5:

        for i in range(3):

            row = sudoku_grid[i+3]

            for j in range(3):

                square.append(row[j]+3)

    if square_n == 6:

        for i in range(3):

            row = sudoku_grid[i+3]

            for j in range(3):

                square.append(row[j+6])

    if square_n == 7:

        for i in range(3):

            row = sudoku_grid[i+6]

            for j in range(3):

                square.append(row[j])

    if square_n == 8:

        for i in range(3):

            row = sudoku_grid[i+6]

            for j in range(3):

                square.append(row[j+3])


    if square_n == 9:

        for i in range(3):

            row = sudoku_grid[i+6]

            for j in range(3):

                square.append(row[j+6])

    return square

def check_grid():

    valid_grid = True

    #get all columns

    columns = []

    for i in range(9):

        columns.append(get_column(i))

    print(columns)

    #get all squares

    squares = []

    for i in range(1,10):

        squares.append(get_square(i))

    print(squares)

    #check rows

    for row in sudoku_grid:

        set_row = set(row)

        #print(set_row)

        if len(set_row) == 9:

            print("valid row")
        else:
            valid_grid = False

            print("invalid row")
            return valid_grid

    #check columns

    for column in columns:

        set_column = set(column)

        if len(set_column) == 9:

            print("valid column")
        else:
            valid_grid = False

            print("invalid column")
            return valid_grid

    #check squares

    for square in squares:

        set_square = set(square)

        if len(set_square) == 9:

            print("valid square")
        else:
            valid_grid = False

            print("invalid square")
            return valid_grid

    return valid_grid
