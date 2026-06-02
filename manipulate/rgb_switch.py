from PIL import Image

img = Image.open("strawberry.png")
img.load()

r, g, b = img.split()

img1 = img.split()

img1 = Image.merge('RGB', (g, r, b))
img1.show()