from editor import get_prompts, make_meme, get_format_titles
from tornado.web import RequestHandler, Application
from twitter_handler import send_image
import tornado.ioloop

class TitlesHandler(RequestHandler):
    def get(self):
        self.write(get_format_titles())
    def set_default_headers(self):
        self.set_header("Access-Control-Allow-Origin", "*")
        self.set_header("Access-Control-Allow-Headers", "x-requested-with")
        self.set_header('Access-Control-Allow-Methods', 'POST, GET, OPTIONS')


class PromptHandler(RequestHandler):
    def set_default_headers(self):
        self.set_header("Access-Control-Allow-Origin", "*")
        self.set_header("Access-Control-Allow-Headers", "x-requested-with")
        self.set_header('Access-Control-Allow-Methods', 'POST, GET, OPTIONS')
    def get(self):
        meme_type = self.get_arguments("title")
        if meme_type == []:
            self.set_status(400)
            return self.finish("Inalid meme title")
        print(meme_type)
        self.write(get_prompts(meme_type[0]))

class MemeGenHandler(RequestHandler):
        def set_default_headers(self):
            self.set_header("Access-Control-Allow-Origin", "*")
            self.set_header("Access-Control-Allow-Headers", "x-requested-with")
            self.set_header('Access-Control-Allow-Methods', 'POST, GET, OPTIONS')
        # need format, text, and caption (for tweeting)
        def get(self):
            meme_format = self.get_arguments("format")
            text = self.get_arguments("text")
            caption = self.get_arguments("caption")
            if format == []:
                self.set_status(400)
                return self.finish("No format given")
            meme_format = meme_format[0]
            caption = "" if caption == [] else caption[0]
            if make_meme(meme_format, text, output='result', show=True):
                print("Meme made, sending tweet")
                send_image('result.jpg', caption)
            self.write("")
if __name__ == "__main__":
    app = Application([
        (r"/titles", TitlesHandler),
        (r"/prompts", PromptHandler),
        (r"/generate", MemeGenHandler)
    ])
    app.listen(8881)
    print("Running on port 8881")
    tornado.ioloop.IOLoop.current().start()
