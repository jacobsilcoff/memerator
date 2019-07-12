from editor import get_prompts, make_meme, get_format_titles
from tornado.web import RequestHandler, Application
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
        self.write(get_prompts(meme_type[0]))


class MemeGenHandler(RequestHandler):
        def set_default_headers(self):
            self.set_header("Access-Control-Allow-Origin", "*")
            self.set_header("Access-Control-Allow-Headers", "x-requested-with")
            self.set_header('Access-Control-Allow-Methods', 'POST, GET, OPTIONS')

if __name__ == "__main__":
    app = Application([
        (r"/titles", TitlesHandler),
        (r"/prompts", PromptHandler)
    ])
    app.listen(8881)
    print("Running on port 8881")
    tornado.ioloop.IOLoop.current().start()
