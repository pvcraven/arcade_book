import random

# These constants are used to determine what should be stored in the grid if we have an empty
# space or a filled space.
EMPTY = "   "
WALL = "XXX"

# Maze must have an ODD number of rows and columns.
# Walls go on EVEN rows/columns.
# Openings go on ODD rows/columns
MAZE_HEIGHT = 51
MAZE_WIDTH = 51


def create_grid(width, height):
    """ Create an empty grid. """
    grid = []
    for row in range(height):
        grid.append([])
        for column in range(width):
            grid[row].append(EMPTY)
    return grid


def print_maze(maze):
    """ Print the maze. """

    # Loop each row, but do it in reverse so 0 is at the bottom like we expect
    for row in range(len(maze) - 1, -1, -1):
        # Print the row/y number
        print(f"{row:3} - ", end="")

        # Loop the row and print the content
        for column in range(len(maze[row])):
            print(f"{maze[row][column]}", end="")

        # Go down a line
        print()

    # Print the column/x at the bottom
    print("     ", end="")
    for column in range(len(maze[0])):
        print(f"{column:3}", end="")
    print()


def create_outside_walls(maze):
    """ Create outside border walls."""

    # Create left and right walls
    for row in range(len(maze)):
        maze[row][0] = WALL
        maze[row][len(maze[row])-1] = WALL

    # Create top and bottom walls
    for column in range(1, len(maze[0]) - 1):
        maze[0][column] = WALL
        maze[len(maze[0]) - 1][column] = WALL


def create_maze(maze, top, bottom, left, right):
    """
    Recursive function to divide up the maze in four sections
    and create three gaps.
    Walls can only go on even numbered rows/columns.
    Gaps can only go on odd numbered rows/columns.
    Maze must have an ODD number of rows and columns.
    """

    # Figure out where to divide horizontally
    start_range = bottom + 2
    end_range = top - 1
    y = random.randrange(start_range, end_range, 2)

    # Do the division
    for column in range(left + 1, right):
        maze[y][column] = WALL

    # Figure out where to divide vertically
    start_range = left + 2
    end_range = right - 1
    x = random.randrange(start_range, end_range, 2)

    # Do the division
    for row in range(bottom + 1, top):
        maze[row][x] = WALL

    # Now we'll make a gap on 3 of the 4 walls.
    # Figure out which wall does NOT get a gap.
    wall = random.randrange(4)
    if wall != 0:
        gap = random.randrange(left + 1, x, 2)
        maze[y][gap] = EMPTY

    if wall != 1:
        gap = random.randrange(x + 1, right, 2)
        maze[y][gap] = EMPTY

    if wall != 2:
        gap = random.randrange(bottom + 1, y, 2)
        maze[gap][x] = EMPTY

    if wall != 3:
        gap = random.randrange(y + 1, top, 2)
        maze[gap][x] = EMPTY

    # Print what's going on
    print(f"Top/Bottom: {top}, {bottom} Left/Right: {left}, {right} Divide: {x}, {y}")
    print_maze(maze)
    print()

    # If there's enough space, to a recursive call.
    if top > y + 3 and x > left + 3:
        create_maze(maze, top, y, left, x)

    if top > y + 3 and x + 3 < right:
        create_maze(maze, top, y, x, right)

    if bottom + 3 < y and x + 3 < right:
        create_maze(maze, y, bottom, x, right)

    if bottom + 3 < y and x > left + 3:
        create_maze(maze, y, bottom, left, x)


def main():

    # Create the blank grid
    maze = create_grid(MAZE_WIDTH, MAZE_HEIGHT)

    # Fill in the outside walls
    create_outside_walls(maze)

    # Start the recursive process
    create_maze(maze, MAZE_HEIGHT - 1, 0, 0, MAZE_WIDTH - 1)


if __name__ == "__main__":
    main()
