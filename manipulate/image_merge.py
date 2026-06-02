from PIL import Image

img1 = Image.open("greece.png")
img2 = Image.open("strawberry.png")
img3 = Image.open("cat.png")
img4 = Image.open("ocean.png")

img1_size = img1.size
img2_size = img2.size
img3_size = img3.size
img4_size = img4.size

print("size of img 1: ", img1.size)
print("size of img 2: ", img2.size)
print("size of img 3: ", img3.size)
print("size of img 4: ", img4.size)

new_im = Image.new('RGB', (2*img1_size[0],2*img1_size[1]), (250,250,250))

new_im.paste(img1, (0,0))
new_im.paste(img2, (img1_size[0],0))
new_im.paste(img3, (0,img1_size[1]))
new_im.paste(img4, (img1_size[0],img1_size[1]))

new_im.show()