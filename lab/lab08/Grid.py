class Grid:
    """
    2D grid with (x, y) int indexed internal storage
    Has .width .height size properties
    """
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
        if x <= self.width and y <= self.height:
            return True
        else:
            print(f"Input ({x}, {y}) is out of bounds!")
            return False

    def get(self, x, y):
        if self.in_bounds(x,y):
            return self.array[y-1][x-1]

    def set(self, x, y, val):
        if self.in_bounds(x,y):
            self.array[y-1][x-1] = val
        return self.array[y-1]

    def __str__(self):
        return f"Grid({self.height}, {self.width}, first = {self.array[0][0]}"

    def __repr__(self):
        return f"Grid({self.height}, {self.width}, first = {self.array[0][0]}"

    def __eq__(self, other):
        if isinstance(other, Grid):
            return self.array == other.array
        else:
            return False
