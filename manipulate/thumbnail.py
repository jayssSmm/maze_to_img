from PIL import Image

# creating a object
image = Image.open("greece.png")
MAX_SIZE = (100, 100)

# Creating the thumbnail
image.thumbnail(MAX_SIZE)

image.show()