from copy import deepcopy


class Grid:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.array = []
        counter_y = 0
        while counter_y < self.height:
            counter_x = 0
            array_row = []
            while counter_x < self.width:
                array_row.append(None)
                counter_x += 1
            self.array.append(array_row)
            counter_y += 1

    def in_bounds(self, x, y):
        if 0 <= abs(x) < self.width and 0 <= abs(y) < self.height:
            return True
        else:
            return False

    def get(self, x, y):
        if self.in_bounds(x, y):
            return self.array[y][x]
        else:
            raise IndexError(f"({x}, {y}) is out of bounds!")

    def set(self, x, y, val):
        if self.in_bounds(x, y):
            self.array[y][x] = val
        else:
            raise IndexError(f"({x}, {y}) is out of bounds!")

    def __str__(self):
        return f"Grid({self.height}, {self.width}, first = {self.array[0][0]})"

    def __repr__(self):
        return f"Grid.build({self.array})"

    def __eq__(self, other):
        if isinstance(other, Grid):
            return self.array == other.array
        elif isinstance(other, list):
            return self.array == other
        else:
            return False

    def copy(self):
        return Grid.build(self.array)

    @staticmethod
    def check_list_malformed(lst):
        if isinstance(lst, list):
            if lst:
                for row in lst:
                    if not isinstance(row, list) or len(row) != len(lst[0]):
                        raise ValueError("Rows are not lists of equal length!")
            else:
                raise ValueError("The list is empty!")
        else:
            raise ValueError("This is not a list!")

    @staticmethod
    def build(lst):
        Grid.check_list_malformed(lst)
        lst_height = len(lst)
        lst_width = len(lst[0])
        new_grid = Grid(lst_width, lst_height)
        new_grid.array = deepcopy(lst)
        return new_grid
