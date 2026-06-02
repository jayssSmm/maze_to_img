from PIL import Image

img = Image.open("strawberry.png")

width, height = img.size

left = 4
top = height/5
right = 154
bottom = 3*height/5

img1 = img.crop((left, top, right, bottom))
newsize = (300, 300)
img1 = img1.resize(newsize)

img1.show()

img.close()
img1.close()