from image_utils import ImageText
import json
import os
from PIL import Image, ImageFont, ImageDraw

#
#   Adds a single textbox to a meme
#
def add_box(template, img, index, text, output):
    font = template["font"]
    width = template["textboxes"][index]["width"]
    height = template["textboxes"][index]["height"]
    x = template["textboxes"][index]["x"]
    y = template["textboxes"][index]["y"]
    img.write_text_box((x,y), text, box_width=width,box_height=height,
    font_filename=font, font_size=32, place='center')
    #img.save(output)
    #img.show()

### CLI:
print("Welcome to memerator.")
answer = None
while True:
    answer = input("Which format would you like? ").casefold() + ".json"
    if (any(map(lambda s : s == answer, os.listdir('templates')))):
        break

#read json file
with open("templates/" + answer, 'r') as f:
    selected_template = json.load(f)
img = ImageText(selected_template["pic"])
add_box(selected_template, img, 0,  "this is the text that i am writing. it is very long! lorem ipsum dolor set amat", 'sample.png')
add_box(selected_template, img, 1,  "this is more text that i am writing. it is also very long! lorem ipsum dolor set amat", 'sample.png')
img.show()
