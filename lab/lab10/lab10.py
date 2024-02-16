from Grid import Grid
import random

test_grid = Grid.build([[None, None, None], [None, None, None], [None, None, None]])


def print_grid(grid):
    """Prints a Grid object with all the elements of a row
    on a single line separated by spaces.
    """
    for y in range(grid.height):
        for x in range(grid.width):
            print(grid.get(x, y) if grid.get(x, y) is not None else 0, end=" ")
        print()
    print()


def random_rocks(grid, chance_of_rock):
    '''Take a grid, loop over it and add rocks randomly
    then return the new grid. If there is something already
    in a grid position, don't add anything in that position.'''
    "*** YOUR CODE HERE ***"
    rock_grid = Grid.build(grid.array.copy())
    # for y in range(rock_grid.height):
    #     for x in range(rock_grid.width):
    #         if not rock_grid.get(x, y) and random.random() <= chance_of_rock:
    #             rock_grid.set(x, y, 'r')
    # return rock_grid
    return modify_grid(rock_grid, lambda x, y: rock_grid.set(x, y, 'r'), chance_of_rock)


def random_bubbles(grid, chance_of_bubbles):
    '''Take a grid, loop over it and add bubbles 'b' randomly
    then return the new grid. If there is something already
    in a grid position, don't add anything in that position.'''
    "*** YOUR CODE HERE ***"
    bubble_grid = Grid.build(grid.array.copy())
    # for y in range(bubble_grid.height):
    #     for x in range(bubble_grid.width):
    #         if not bubble_grid.get(x, y) and random.random() <= chance_of_bubbles:
    #             bubble_grid.set(x, y, 'b')
    # return bubble_grid
    return modify_grid(bubble_grid, lambda x, y: bubble_grid.set(x, y, 'b'), chance_of_bubbles)


def modify_grid(grid, func, prob):
    """Write a function which can take in a grid, a function
    and a probablily as parameters and updates the grid using
    the function passed in."""
    "*** YOUR CODE HERE ***"
    for y in range(grid.height):
        for x in range(grid.width):
            if not grid.get(x, y) and random.random() <= prob:
                func(x, y)
    return grid


def bubble_up(grid, x, y):
    """
    Write a function that takes a bubble that is known
    to be able to bubble up and moves it up one row.
    """
    "*** YOUR CODE HERE ***"
    bubble_up_grid = Grid.build(grid.array.copy())
    bubble_up_grid.set(x, y - 1, grid.get(x, y))
    bubble_up_grid.set(x, y, None)
    return bubble_up_grid


def move_bubbles(grid):
    """
    Write a function that loops over the grid, finds
    bubbles, checks if the bubble can move upward, moves
    the bubble up.
    """
    move_bubbles_grid = Grid.build(grid.array.copy())
    for y in range(move_bubbles_grid.height):
        for x in range(move_bubbles_grid.width):
            if move_bubbles_grid.get(x, y) == 'b' and y != 0:
                if not move_bubbles_grid.get(x, y - 1):
                    move_bubbles_grid = bubble_up(move_bubbles_grid, x, y)
    return move_bubbles_grid


def animate_grid(grid, delay):
    """Given an Grid object, and a delay time in seconds, this
    function prints the current grid contents (calls print_grid),
    waits for `delay` seconds, calls the move_bubbles() function,
    and repeats until the grid doesn't change.
    """
    from time import sleep
    prev = grid
    count = 0
    message = "Start"
    while True:
        print("\033[2J\033[;H", end="")
        message = f"Iteration {count}"
        print(message)
        print_grid(prev)
        sleep(delay)
        newGrid = move_bubbles(prev)
        if newGrid == prev:
            break
        prev = newGrid
        count += 1
