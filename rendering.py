from PIL import Image, ImageFont, ImageDraw

img = Image.open("background.png")
# font = ImageFont.truetype(font, size)
font = ImageFont.truetype(font="impact.ttf", size=150)

draw = ImageDraw.Draw(img)

text = "Hello there"
draw.text((150, 150), text, (255, 255, 255), font=font)
img.save("text.png")