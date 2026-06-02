from PIL import Image, ImageDraw

square_size = 80
board_size = 8

img = Image.new('RGB', (square_size * board_size,
                        square_size * board_size))

draw = ImageDraw.Draw(img)

light = (240, 217, 181)
dark = (181, 136, 99)

for i in range(8):
    for j in range(8):
        color = light if (i + j)%2 == 0 else dark

        x1 = j * square_size
        y1 = i * square_size
        x2 = x1 + square_size
        y2 = y1 + square_size

        draw.rectangle([x1, y1, x2, y2], fill = color)

img.show()