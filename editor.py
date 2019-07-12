from image_utils import ImageText
import json
import os
from PIL import Image, ImageFont, ImageDraw

#
#   Adds a single textbox to a meme
#
def add_box(template, img, index, text):
    font = template["font"]
    width = template["textboxes"][index]["width"]
    height = template["textboxes"][index]["height"]
    x = template["textboxes"][index]["x"]
    y = template["textboxes"][index]["y"]
    img.write_text_box((x,y), text, box_width=width,box_height=height,
    color=template["text_color"], font_filename=font, font_size=32,
    place='center', shadowcolor=template["dropshadow"])
    #img.save(output)
    #img.show()

### CLI:
def run_cli():
    print("Welcome to memerator.")
    answer = None
    while True:
        answer = input("Which format would you like? ").casefold().replace(" ", "") + ".json"
        if (any(map(lambda s : s == answer, os.listdir('templates')))):
            break

    #read json file
    with open("templates/" + answer, 'r') as f:
        selected_template = json.load(f)
    img = ImageText(selected_template["pic"])
    for i in range(0, len(selected_template["textboxes"])):
        txt = input(selected_template["textboxes"][i]["prompt"] + " ")
        add_box(selected_template, img, i,  txt)
    #Show output to person
    img.show()

    #help user to save or not save
    answer = input("Would you like to save your meme? Please enter Y/N: ").casefold()
    while answer not in ["y", "n"]:
        print("Bad input")
        answer = input("Please enter either y or n: ")
    if answer == "y":
        name = input("Please enter name of file to save to: ")
        img.save(name)

### Public Interface:
def get_all_formats():
    opts = os.listdir('templates')
    temp = {}
    for opt in opts:
        with open("templates/" + opt, 'r') as f:
            temp[opt[0:-5]] = json.load(f)
    return temp

def get_format_titles():
    opts = os.listdir('templates')
    temp = {}
    for opt in opts:
        with open("templates/" + opt, 'r') as f:
            temp[opt[0:-5]] = json.load(f)['title']
    return temp

def get_prompts(meme):
    meme = meme.replace(" ", "")
    with open("templates/" + meme + ".json", 'r') as f:
        full_json = json.load(f)
        prompts = list(map(lambda x : {"prompt":x["prompt"]},
                       full_json["textboxes"]))
        return {"title":full_json["title"],
                "text_boxes": prompts}
def make_meme(format, responses, output=None, show=False):
        format = format.replace(" ","") + ".json"
        #read json file
        with open("templates/" + format, 'r') as f:
            selected_template = json.load(f)
        img = ImageText(selected_template["pic"])
        for i,txt in enumerate(responses):
            add_box(selected_template, img, i,  txt)
        #Show output to person
        if show:
            img.show()
        if ouput is not None:
            img.save(output + ".jpg")
