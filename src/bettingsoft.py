import tornado.ioloop
import tornado.web

from handlers import AddHandler, GetHandler, RemoveHandler, UpdateHandler, StatisticHandler
import settings

def make_app():
    return tornado.web.Application([
        (r"/api/add", AddHandler),
        (r"/api/get", GetHandler),
        (r"/api/remove", RemoveHandler),
        (r"/api/update", UpdateHandler),
        (r"/api/statistic", StatisticHandler),
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(settings.port)
    print('server is running')
    tornado.ioloop.IOLoop.current().start()