from twitter_handler import send_image
from flask import Flask, escape, request
from editor import get_prompts, make_meme, get_format_titles, PATH


app = Flask(__name__)

@app.route('/')
def hello():
    name = request.args.get("name", "World")
    return f'Hello, {escape(name)}!'

@app.route('/titles')
def titles():
    return get_format_titles()

@app.route('/prompts')
def prompts():
    meme_type = request.args.get("title", "")
    return get_prompts(meme_type)

@app.route('/generate')
def generate():
    meme_format = request.args.get("format", None)
    text = request.args.getlist("text")
    caption = request.args.get("caption", "")
    if format == None:
        return "No good!"
    try:
        make_meme(meme_format, text, output='result')
    except Exception as e:
        return "Error Encountered, failed to send: " + str(e)
    send_image('/home/jacobsilcoff/memerator/result.jpg', caption)
    return "Send tweet!"