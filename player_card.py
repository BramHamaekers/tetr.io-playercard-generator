from PIL import Image, ImageFont, ImageDraw


def render(data: dict):
    img = Image.open("background.png")
    draw = ImageDraw.Draw(img)

    # Set user and data fonts
    user_font = ImageFont.truetype(font="bahnschrift.ttf", size=144)
    user_font.set_variation_by_name('Bold SemiCondensed')
    data_font = ImageFont.truetype(font="bahnschrift.ttf", size=108)
    data_font.set_variation_by_name('Bold SemiCondensed')

    # Set standard text positions
    center = 1920 / 2  # get center position to draw name text
    top = 85
    left = 400
    right = 1920 - left
    data_top = 430

    # Draw username
    text = data.get('username')
    text = text.upper()
    draw.text((center, top), text, (255, 255, 255), font=user_font, anchor="ma")
    draw.text((center - 7, top - 7), text, (255, 195, 30), font=user_font, anchor="ma")

    # Draw data
    data_elements = ['tr', 'pps', 'apm', 'vs']
    for elem in data_elements:
        text: str = str(data.get(elem))
        draw.text((left, data_top), elem.upper(), (255, 255, 255), font=data_font, anchor="la")
        draw.text((left - 7, data_top - 7), elem.upper(), (255, 195, 30), font=data_font, anchor="la")
        draw.text((right, data_top), text, (255, 255, 255), font=data_font, anchor="ra")
        data_top += 150

    img.save("text.png")
