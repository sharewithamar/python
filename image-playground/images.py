from PIL import Image, ImageFilter

img = Image.open("./astro.jpg")

# use thumbnail to presever aspect ratio instead of resize
img.thumbnail((400, 400))
img.save('thumbnail.jpg')
# 400*380 - intelligently decides whats the best size for the image  within the range
print(img.size)

#img = Image.open("./pokedex/pikachu.jpg")
#filtered_img = img.filter(ImageFilter.SHARPEN)
# filtered_img = img.convert('L')
# box = (100, 100, 400, 400)
# region = filtered_img.crop(box)
#region.save("grey.png", 'png')
# resize = filtered_img.resize((300, 300))
# resize.save("grey.png", 'png')
# crooked = filtered_img.rotate(90)
# crooked.save("grey.png", 'png')
#filtered_img.save("grey.png", 'png')
# filtered_img.show()  # opens the image in photos
#filtered_img.save("sharpen.png", 'png')

# remember to use dir to find the list of methods,properties we can use
# print(dir(img))
