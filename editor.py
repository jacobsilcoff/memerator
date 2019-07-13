from image_utils import ImageText
import json
import os
from PIL import Image, ImageFont, ImageDraw

PATH = "/home/jacobsilcoff/memerator/"

#
#   Adds a single textbox to a meme
#
def add_box(template, img, index, text):
    font = PATH + template["font"]
    width = template["textboxes"][index]["width"]
    height = template["textboxes"][index]["height"]
    x = template["textboxes"][index]["x"]
    y = template["textboxes"][index]["y"]
    img.write_text_box((x,y), text, box_width=width,box_height=height,
    color=template["text_color"], font_filename=font, font_size=32,
    place='center', shadowcolor=template["dropshadow"])
    #img.save(output)
    #img.show()

### Public Interface:
def get_all_formats():
    opts = os.listdir('/home/jacobsilcoff/memerator/templates')
    temp = {}
    for opt in opts:
        with open("/home/jacobsilcoff/memerator/templates/" + opt, 'r') as f:
            temp[opt[0:-5]] = json.load(f)
    return temp

def get_format_titles():
    opts = os.listdir('/home/jacobsilcoff/memerator/templates')
    temp = {}
    for opt in opts:
        with open("/home/jacobsilcoff/memerator/templates/" + opt, 'r') as f:
            temp[opt[0:-5]] = json.load(f)['title']
    return temp

def get_prompts(meme):
    meme = meme.replace(" ", "")
    with open("/home/jacobsilcoff/memerator/templates/" + meme + ".json", 'r') as f:
        full_json = json.load(f)
        prompts = list(map(lambda x : {"prompt":x["prompt"]},
                       full_json["textboxes"]))
        return {"title":full_json["title"],
                "text_boxes": prompts}
def make_meme(format, responses, output=None):
    format = format.replace(" ","") + ".json"
    #read json file
    f = open("/home/jacobsilcoff/memerator/templates/" + format, 'r')
    selected_template = json.load(f)
    img = ImageText(PATH + selected_template["pic"])
    for i,txt in enumerate(responses):
        add_box(selected_template, img, i,  txt)
    if output is not None:
        img.save("/home/jacobsilcoff/memerator/" + output + ".jpg")

