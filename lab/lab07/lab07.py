class Button:
    def __init__(self, pos, key):
        self.pos = pos
        self.key = key
        self.times_pressed = 0

    def __str__(self):
        return f"Key: '{self.key}', Pos: {self.pos}"

    def __repr__(self):
        return f"Button({self.pos}, '{self.key}')"


class Keyboard:
    """A Keyboard takes in an arbitrary amount of buttons, and has a
    dictionary of positions as keys, and values as Buttons.
    >>> b1 = Button(0, "H")
    >>> b2 = Button(1, "I")
    >>> k = Keyboard(b1, b2)
    >>> k.buttons[0].key
    'H'
    >>> k.press(1)
    'I'
    >>> k.press(2) # No button at this position
    ''
    >>> k.typing([0, 1])
    'HI'
    >>> k.typing([1, 0])
    'IH'
    >>> b1.times_pressed
    2
    >>> b2.times_pressed
    3
    """
    def __init__(self, *args):
        self.buttons = {}
        for button in args:
            self.buttons[button.pos] = button

    def press(self, info):
        """Takes in a position of the button pressed, and
        returns that button's output."""
        if info in self.buttons:
            button = self.buttons[info]
            button.times_pressed += 1
            return button.key
        else:
            return ""

    def typing(self, typing_input):
        """Takes in a list of positions of buttons pressed, and
        returns the total output."""
        total_output = ""
        for position in typing_input:
            total_output += self.press(position)
        return total_output

    def add_button(self, button):
        """Adds a button to the keyboard if the position is not taken"""
        if ____________________:
            ________________
            ________________
        ________________

    def __str__(self):
        return_string = ""
        counter = 0
        for button in self.buttons.keys():
            return_string += str(button)
            if counter < len(self.buttons) - 1:
                return_string += " | "
                counter += 1
            return_string += ""
        return return_string

    def __repr__(self):
        return_string = "Keyboard("
        counter = 0
        for button in self.buttons.keys():
            return_string += repr(button)
            if counter < len(self.buttons) - 1:
                return_string += ", "
                counter += 1
            return_string += ")"
        return return_string


b1 = Button(0, "H")
b2 = Button(1, "I")
k = Keyboard(b1, b2)
print(k)
