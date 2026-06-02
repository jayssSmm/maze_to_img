from PIL import Image

img = Image.open("strawberry")

'''
print(img.size)
print(img.format)
print(img.mode)

img1= img.rotate(90, PIL.Image.NEAREST, expand=1)
'''

img1 = img.transpose(method=Image.FLIP_TOP_BOTTOM)
img1.save("flip_strawberry.jpg")

img1.show()

img.close()
img1.close()