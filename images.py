from PIL import Image, ImageEnhance



image = Image.open("InputFile.png")
image.show()

contrast = ImageEnhance.Contrast(image)
bright = ImageEnhance.Brightness(image)

print("Enter the contrast factor: ")
c_change = float(input())
print("Enter the brightness factor: ")
b_change = float(input())

c_image = contrast.enhance(c_change)
b_image = bright.enhance(b_change)

c_image.show(title = "Contrast")
b_image.show(title = "Bright")
c_b_image = ImageEnhance.Contrast(b_image).enhance(c_change)
c_b_image.show(title = "Contrast + Bright")

c_b_image.save("OutFile.png")
