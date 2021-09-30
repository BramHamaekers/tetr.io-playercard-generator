from PIL import Image, ImageFont, ImageDraw

img = Image.open("background.png")
# font = ImageFont.truetype(font, size)
font = ImageFont.truetype(font="bahnschrift.ttf", size=150)
font.set_variation_by_name('Bold SemiCondensed')

draw = ImageDraw.Draw(img)

text = "AwoOie"
text = text.upper()
w, h = draw.textsize(text)  # get size of name
print(w)
center_pos = (1920 - round(11.8*w))/2
print(center_pos)


draw.text((center_pos, 190), text, (255, 255, 255), font=font)
draw.text((center_pos - 9, 181), text, (255, 195, 30), font=font)
img.save("text.png")