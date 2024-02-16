# IMPORTANT - Remember to import Image from the byuimage library: `from byuimage import Image`
from byuimage import Image


def iron_puzzle(filename):
    "*** YOUR CODE HERE ***"
    image = Image(filename)
    new_image = Image.blank(image.width, image.height)
    for y in range(image.height):
        for x in range(image.width):
            pixel = image.get_pixel(x, y)
            new_pixel = new_image.get_pixel(x, y)
            new_pixel.red = pixel.red * 0
            new_pixel.green = pixel.green * 0
            new_pixel.blue = pixel.blue * 10
    return new_image


# solution_image = iron_puzzle("test_files/iron.png")
# solution_image.show()


def west_puzzle(filename):
    "*** YOUR CODE HERE ***"
    image = Image(filename)
    new_image = Image.blank(image.width, image.height)
    for y in range(image.height):
        for x in range(image.width):
            pixel = image.get_pixel(x, y)
            new_pixel = new_image.get_pixel(x, y)
            new_pixel.red = pixel.red * 0
            new_pixel.green = pixel.green * 0
            if pixel.blue < 16:
                new_pixel.blue = pixel.blue * 16
            else:
                new_pixel.blue = pixel.blue * 0
    return new_image


# solution = west_puzzle("test_files/west.png")
# solution.show()


def darken(filename, percent):
    "*** YOUR CODE HERE ***"
    image = Image(filename)
    new_image = Image.blank(image.width, image.height)
    dark = 1 - percent
    for y in range(image.height):
        for x in range(image.width):
            pixel = image.get_pixel(x, y)
            new_pixel = new_image.get_pixel(x, y)
            new_pixel.red = pixel.red * dark
            new_pixel.green = pixel.green * dark
            new_pixel.blue = pixel.blue * dark
    return new_image


solution_darken = darken("test_files/cougar.png", 0.6)
solution_darken.show()


def grayscale(filename):
    "*** YOUR CODE HERE ***"
    image = Image(filename)
    new_image = Image.blank(image.width, image.height)
    for y in range(image.height):
        for x in range(image.width):
            pixel = image.get_pixel(x, y)
            new_pixel = new_image.get_pixel(x, y)
            average = (pixel.red + pixel.green + pixel.blue) / 3
            new_pixel.red = average
            new_pixel.green = average
            new_pixel.blue = average
    return new_image


# gray = grayscale("test_files/cougar.png")
# gray.show()


def sepia(filename):
    "*** YOUR CODE HERE ***"
    image = Image(filename)
    new_image = Image.blank(image.width, image.height)
    for y in range(image.height):
        for x in range(image.width):
            pixel = image.get_pixel(x, y)
            new_pixel = new_image.get_pixel(x, y)
            true_red = 0.393 * pixel.red + 0.769 * pixel.green + 0.189 * pixel.blue
            true_green = 0.349 * pixel.red + 0.686 * pixel.green + 0.168 * pixel.blue
            true_blue = 0.272 * pixel.red + 0.534 * pixel.green + 0.131 * pixel.blue
            new_pixel.red = true_red
            if new_pixel.red > 255:
                new_pixel.red = 255
            new_pixel.green = true_green
            if new_pixel.green > 255:
                new_pixel.green = 255
            new_pixel.blue = true_blue
            if new_pixel.blue > 255:
                new_pixel.blue = 255
    return new_image


# solution_sepia = sepia("test_files/cougar.png")
# solution_sepia.show()


def create_left_border(filename, weight):
    "*** YOUR CODE HERE ***"
    image = Image(filename)
    new_image = Image.blank(image.width + weight, image.height)
    for y in range(image.height):
        for x in range(weight, image.width + weight):
            pixel = image.get_pixel(x - weight, y)
            new_pixel = new_image.get_pixel(x, y)
            average = (pixel.red + pixel.green + pixel.blue) / 3
            new_pixel.red = pixel.red
            new_pixel.green = pixel.green
            new_pixel.blue = pixel.blue
        for x in range(weight):
            new_pixel = new_image.get_pixel(x, y)
            new_pixel.red = 0
            new_pixel.green = 0
            new_pixel.blue = 255
    return new_image


# solution_border = create_left_border("test_files/cougar.png", 25)
# solution_border.show()

###################################################
# Code below here is for extra practice and doesn't count for or against
# your grade on this lab.
def create_stripes(filename):
    "*** YOUR CODE HERE ***"
    image = Image(filename)
    new_image = Image.blank(image.width + 50, image.height + 25)
    for y in range(image.height + 25):
        for x in range(image.width + 50):
            new_pixel = new_image.get_pixel(x, y)
            if y % 2 == 0:
                new_pixel.red = 0
                new_pixel.green = 255
                new_pixel.blue = 0
            elif x % 2 != 0:
                new_pixel.red = 0
                new_pixel.green = 0
                new_pixel.blue = 255
            else:
                new_pixel.red = 255
                new_pixel.green = 0
                new_pixel.blue = 0
    return new_image


# solution_stripes = create_stripes("test_files/cougar.png")
# solution_stripes.show()


def copper_puzzle(filename):
    "*** YOUR CODE HERE ***"
    image = Image(filename)
    new_image = Image.blank(image.width, image.height)
    for y in range(image.height):
        for x in range(image.width):
            pixel = image.get_pixel(x, y)
            new_pixel = new_image.get_pixel(x, y)
            new_pixel.red = pixel.red * 0
            new_pixel.green = pixel.green * 20
            new_pixel.blue = pixel.blue * 20
    return new_image


# solution_copper = copper_puzzle("test_files/copper.png")
# solution_copper.show()
