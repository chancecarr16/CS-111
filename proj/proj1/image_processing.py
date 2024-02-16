# Functions go here:
import sys
from byuimage import Image

commands = ["-d", "-k", "-s", "-g", "-b", "-f", "-m", "-c", "-y"]


def validate_commands(arg):
    if arg in commands:
        return True
    else:
        return False


def image_commands(arg):
    if arg[1] == "-d" and len(arg) > 2:
        display(arg[2])
    elif arg[1] == "-k" and len(arg) > 4:
        darken(arg[2], arg[3], arg[4])
    elif arg[1] == "-s" and len(arg) > 3:
        sepia(arg[2], arg[3])
    elif arg[1] == "-g" and len(arg) > 3:
        grayscale(arg[2], arg[3])
    elif arg[1] == "-b" and len(arg) > 7:
        make_borders(arg[2], arg[3], arg[4], arg[5], arg[6], arg[7])
    elif arg[1] == "-f" and len(arg) > 3:
        flipped(arg[2], arg[3])
    elif arg[1] == "-m" and len(arg) > 3:
        mirrored(arg[2], arg[3])
    elif arg[1] == "-c" and len(arg) > 7:
        collage(arg[2], arg[3], arg[4], arg[5], arg[6], arg[7])
    elif arg[1] == "-y" and len(arg) > 6:
        green_screen(arg[2], arg[3], arg[4], arg[5], arg[6])
    else:
        return False


def read_in(filename):
    image = Image(filename)
    return image


def display(filename):
    image = read_in(filename)
    image.show()


def filter_image(filename, red, green, blue):
    image = read_in(filename)
    new_image = Image.blank(image.width, image.height)
    for y in range(image.height):
        for x in range(image.width):
            pixel = image.get_pixel(x, y)
            new_pixel = new_image.get_pixel(x, y)
            new_pixel.red = pixel.red * red
            new_pixel.green = pixel.green * green
            new_pixel.blue = pixel.blue * blue
            if new_pixel.red > 255:
                new_pixel.red = 255
            if new_pixel.green > 255:
                new_pixel.green = 255
            if new_pixel.blue > 255:
                new_pixel.blue = 255
    return new_image


def darken(filename, output_file, percent):
    dark = 1 - float(percent)
    new_image = filter_image(filename, dark, dark, dark)
    new_image.save(output_file)


def sepia(filename, output_file):
    image = read_in(filename)
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
    new_image.save(output_file)


def grayscale(filename, output_file):
    image = read_in(filename)
    new_image = Image.blank(image.width, image.height)
    for y in range(image.height):
        for x in range(image.width):
            pixel = image.get_pixel(x, y)
            new_pixel = new_image.get_pixel(x, y)
            average = (pixel.red + pixel.green + pixel.blue) / 3
            new_pixel.red = average
            new_pixel.green = average
            new_pixel.blue = average
    new_image.save(output_file)


def make_borders(filename, output_file, thickness, red, green, blue):
    image = read_in(filename)
    thickness = int(thickness)
    red = int(red)
    green = int(green)
    blue = int(blue)
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
    border_image.save(output_file)


def flipped(filename, output_file):
    image = read_in(filename)
    flipped_image = Image.blank(image.width, image.height)
    for y in range(image.height):
        for x in range(image.width):
            pixel = image.get_pixel(x, y)
            flipped_pixel = flipped_image.get_pixel(x, ((y - image.height) * -1 - 1))
            flipped_pixel.red = pixel.red
            flipped_pixel.green = pixel.green
            flipped_pixel.blue = pixel.blue
    flipped_image.save(output_file)


def mirrored(filename, output_file):
    image = read_in(filename)
    mirrored_image = Image.blank(image.width, image.height)
    for y in range(image.height):
        for x in range(image.width):
            pixel = image.get_pixel(x, y)
            mirrored_pixel = mirrored_image.get_pixel(((x - image.width) * -1 - 1), y)
            mirrored_pixel.red = pixel.red
            mirrored_pixel.green = pixel.green
            mirrored_pixel.blue = pixel.blue
    mirrored_image.save(output_file)


def collage(image_1, image_2, image_3, image_4, output_file, thickness):
    image_1 = read_in(image_1)
    image_2 = read_in(image_2)
    image_3 = read_in(image_3)
    image_4 = read_in(image_4)
    thickness = int(thickness)
    new_image = Image.blank(image_1.width * 2 + (3 * thickness), image_1.height * 2 + (3 * thickness))
    for y in range(thickness):
        for x in range(new_image.width):
            new_pixel = new_image.get_pixel(x, y)
            new_pixel.red = 0
            new_pixel.green = 0
            new_pixel.blue = 0
    for y in range(thickness, image_1.height + thickness):
        for x in range(thickness):
            new_pixel = new_image.get_pixel(x, y)
            new_pixel.red = 0
            new_pixel.green = 0
            new_pixel.blue = 0
        for x in range(thickness, image_1.width + thickness):
            pixel = image_1.get_pixel(x - thickness, y - thickness)
            new_pixel = new_image.get_pixel(x, y)
            new_pixel.red = pixel.red
            new_pixel.green = pixel.green
            new_pixel.blue = pixel.blue
        for x in range(image_1.width + thickness, image_1.width + (2 * thickness)):
            new_pixel = new_image.get_pixel(x, y)
            new_pixel.red = 0
            new_pixel.green = 0
            new_pixel.blue = 0
        for x in range(image_1.width + (2 * thickness), new_image.width - thickness):
            pixel = image_2.get_pixel(x - (image_1.width + (2 * thickness)), y - thickness)
            new_pixel = new_image.get_pixel(x, y)
            new_pixel.red = pixel.red
            new_pixel.green = pixel.green
            new_pixel.blue = pixel.blue
        for x in range(new_image.width - thickness, new_image.width):
            new_pixel = new_image.get_pixel(x, y)
            new_pixel.red = 0
            new_pixel.green = 0
            new_pixel.blue = 0
    for y in range(image_1.height + thickness, image_1.height + (2 * thickness)):
        for x in range(new_image.width):
            new_pixel = new_image.get_pixel(x, y)
            new_pixel.red = 0
            new_pixel.green = 0
            new_pixel.blue = 0
    for y in range(image_1.height + (2 * thickness), new_image.height - thickness):
        for x in range(thickness):
            new_pixel = new_image.get_pixel(x, y)
            new_pixel.red = 0
            new_pixel.green = 0
            new_pixel.blue = 0
        for x in range(thickness, image_1.width + thickness):
            pixel = image_3.get_pixel(x - thickness, y - (image_1.height + (2 * thickness)))
            new_pixel = new_image.get_pixel(x, y)
            new_pixel.red = pixel.red
            new_pixel.green = pixel.green
            new_pixel.blue = pixel.blue
        for x in range(image_1.width + thickness, image_1.width + (2 * thickness)):
            new_pixel = new_image.get_pixel(x, y)
            new_pixel.red = 0
            new_pixel.green = 0
            new_pixel.blue = 0
        for x in range(image_1.width + (2 * thickness), new_image.width - thickness):
            pixel = image_4.get_pixel(x - (image_1.width + (2 * thickness)), y - (image_1.height + (2 * thickness)))
            new_pixel = new_image.get_pixel(x, y)
            new_pixel.red = pixel.red
            new_pixel.green = pixel.green
            new_pixel.blue = pixel.blue
        for x in range(new_image.width - thickness, new_image.width):
            new_pixel = new_image.get_pixel(x, y)
            new_pixel.red = 0
            new_pixel.green = 0
            new_pixel.blue = 0
    for y in range(new_image.height - thickness, new_image.height):
        for x in range(new_image.width):
            new_pixel = new_image.get_pixel(x, y)
            new_pixel.red = 0
            new_pixel.green = 0
            new_pixel.blue = 0
    new_image.save(output_file)


def green_screen(filename, background, output_file, threshold, factor):
    image = read_in(filename)
    background = read_in(background)
    new_image = Image.blank(image.width, image.height)
    threshold = int(threshold)
    factor = float(factor)

    def detect_green(current_pixel):
        average_color = (current_pixel.red + current_pixel.green + current_pixel.blue) / 3
        if current_pixel.green >= average_color * factor and current_pixel.green > threshold:
            return True
        else:
            return False
    for y in range(image.height):
        for x in range(image.width):
            pixel = image.get_pixel(x, y)
            background_pixel = background.get_pixel(x, y)
            new_pixel = new_image.get_pixel(x, y)
            if detect_green(pixel):
                new_pixel.red = background_pixel.red
                new_pixel.green = background_pixel.green
                new_pixel.blue = background_pixel.blue
            else:
                new_pixel.red = pixel.red
                new_pixel.green = pixel.green
                new_pixel.blue = pixel.blue
    new_image.save(output_file)


if __name__ == "__main__":
    if validate_commands(sys.argv[1]):
        image_commands(sys.argv)

