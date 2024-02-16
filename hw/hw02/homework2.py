from byuimage import Image


def flipped(filename):
    image = Image(filename)
    flipped_image = Image.blank(image.width, image.height)
    for y in range(image.height):
        for x in range(image.width):
            pixel = image.get_pixel(x, y)
            flipped_pixel = flipped_image.get_pixel(x, ((y - image.height) * -1 - 1))
            flipped_pixel.red = pixel.red
            flipped_pixel.green = pixel.green
            flipped_pixel.blue = pixel.blue
    return flipped_image


def make_borders(filename, thickness, red, green, blue):
    image = Image(filename)
    border_image = Image.blank(image.width + thickness * 2, image.height + thickness * 2)
    for y in range(image.height + thickness):
        for x in range(thickness):
            border_pixel = border_image.get_pixel(x, y)
            border_pixel.red = red
            border_pixel.green = green
            border_pixel.blue = blue
    for y in range(0, thickness):
        for x in range(0, image.width + thickness):
            border_pixel = border_image.get_pixel(x, y)
            border_pixel.red = red
            border_pixel.green = green
            border_pixel.blue = blue
    for y in range(0, image.height):
        for x in range(0, image.width):
            pixel = image.get_pixel(x, y)
            new_pixel = border_image.get_pixel(x + thickness, y + thickness)
            new_pixel.red = pixel.red
            new_pixel.green = pixel.green
            new_pixel.blue = pixel.blue
    for y in range(0, image.height + (2 * thickness)):
        for x in range(image.width + thickness, image.width + (2 * thickness)):
            border_pixel = border_image.get_pixel(x, y)
            border_pixel.red = red
            border_pixel.green = green
            border_pixel.blue = blue
    for y in range(image.height + thickness, image.height + (2 * thickness)):
        for x in range(0, image.width + (2 * thickness)):
            border_pixel = border_image.get_pixel(x, y)
            border_pixel.red = red
            border_pixel.green = green
            border_pixel.blue = blue
    return border_image


if __name__ == "__main__":
    flipped("test_files/landscape.png")
    test = make_borders("test_files/flamingo-float.png", 30, 0, 0, 0)

