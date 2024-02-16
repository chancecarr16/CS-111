from Grid import Grid

test_grid = Grid(3, 3)

other_grid = Grid(3, 3)

print(test_grid.array)

print(other_grid.array)

print(test_grid.__eq__(other_grid))
