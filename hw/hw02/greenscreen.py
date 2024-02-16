from byuimage import Image


def green_screen(filename, background):
    image = Image(filename)
    background_image = Image(background)
    if background_image.width >= image.width and background_image.height >= image.height:
        new_image = Image.blank(background_image.width, background_image.height)
        buffer_x = (new_image.width - image.width) // 2
        buffer_y = (new_image.height - image.height) // 2
        buffer_background_x = 0
        buffer_background_y = 0
    elif background_image.width >= image.width:
        new_image = Image.blank(background_image.width, image.height)
        print("Your background image isn't tall enough!")
        buffer_x = (new_image.width - image.width) // 2
        buffer_y = 0
        buffer_background_y = (image.height - background_image.height) // 2
        buffer_background_x = 0
        print(f"buffer x: {buffer_x}, buffer bg y: {buffer_background_y}")
    elif background_image.height >= image.height:
        new_image = Image.blank(image.width, background_image.height)
        print("Your background image isn't wide enough!")
        buffer_x = 0
        buffer_y = (new_image.height - image.height) // 2
        buffer_background_x = (image.width - background_image.width) // 2
        buffer_background_y = 0
    else:
        print("Your background image is too small!")
        return image

    def border_color(border_image):
        total_red = 0
        total_green = 0
        total_blue = 0
        for border_y in range(0, 2):
            for border_x in range(border_image.width):
                border_pixel = border_image.get_pixel(border_x, border_y)
                total_red += border_pixel.red
                total_green += border_pixel.green
                total_blue += border_pixel.blue
        average_red = total_red / border_image.width
        average_green = total_green / border_image.width
        average_blue = total_blue / border_image.width
        return average_red, average_green, average_blue

    def detect_green(p):
        factor = 1.15
        average = (p.red + p.blue + p.green) / 3
        if p.green > average * factor and p.green > 60:
            return True
        else:
            return False
    for y in range(new_image.height):
        for x in range(new_image.width):
            print(f"{x}, {y}")
            new_pixel = new_image.get_pixel(x, y)
            if buffer_y <= y <= (new_image.height - buffer_y) and buffer_x <= x <= (new_image.width - buffer_x):
                pixel = image.get_pixel(x - buffer_x - 1, y - buffer_y - 1)
                if buffer_background_y <= y <= (new_image.height - buffer_background_y) and buffer_background_x <= x <= (new_image.width - buffer_background_x):
                    background_pixel = background_image.get_pixel(x - buffer_background_x, y - buffer_background_y)
                    if detect_green(pixel):
                        new_pixel.red = background_pixel.red
                        new_pixel.green = background_pixel.green
                        new_pixel.blue = background_pixel.blue
                    else:
                        new_pixel.red = pixel.red
                        new_pixel.green = pixel.green
                        new_pixel.blue = pixel.blue
                else:
                    if detect_green(pixel):
                        new_pixel.red, new_pixel.green, new_pixel.blue = border_color(background_image)
                    else:
                        new_pixel.red = pixel.red
                        new_pixel.green = pixel.green
                        new_pixel.blue = pixel.blue
            else:
                new_pixel.red, new_pixel.green, new_pixel.blue = border_color(background_image)
    return new_image


solution = green_screen("test_files/man.png", "test_files/mount-fuji.png")
solution.show()
