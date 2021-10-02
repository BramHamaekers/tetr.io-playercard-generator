from PIL import Image, ImageFont, ImageDraw
import os


def render_text(data: dict):
    img = Image.open("background.jpg")
    draw = ImageDraw.Draw(img)

    # Set user and data fonts
    user_font = ImageFont.truetype(font="bahnschrift.ttf", size=144)
    user_font.set_variation_by_name('Bold SemiCondensed')
    country_font = ImageFont.truetype(font="bahnschrift.ttf", size=80)
    country_font.set_variation_by_name('Bold SemiCondensed')
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

    # Temporary draw country
    text = data.get('country')
    print(text)
    text = text.upper()
    draw.text((center, top + 150), text, (255, 255, 255), font=country_font, anchor="ma")

    # Draw data
    data_elements = ['tr', 'pps', 'apm', 'vs']
    for elem in data_elements:
        text: str = str(data.get(elem))
        draw.text((left, data_top), elem.upper(), (255, 255, 255), font=data_font, anchor="la")
        draw.text((left - 7, data_top - 7), elem.upper(), (255, 195, 30), font=data_font, anchor="la")
        draw.text((right, data_top), text, (255, 255, 255), font=data_font, anchor="ra")
        data_top += 150

    img.convert('RGB').save('card.jpg')
    render_rank(data.get('rank'))


def render_rank(rank):
    img = Image.open('card.jpg')
    rank = Image.open('rank_gfx/' + rank + '.jpg')
    img.paste(rank, (1920-485, 85))
    img.save('card.jpg')


def render_avatar():
    img = Image.open('card.jpg')
    try:
        avatar = Image.open('avatar.jpg')
    except FileNotFoundError:
        avatar = Image.open('default_avatar.jpg')
    img.paste(avatar, (185, 85))
    img.save('card.jpg')
    img.show()
    try:
        os.remove('avatar.jpg')
    except FileNotFoundError:
        return
