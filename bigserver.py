import tornado.httpserver
import tornado.websocket
import tornado.ioloop
import tornado.web
from tornado import websocket, web, ioloop
import json

cl = []

class SocketHandler(websocket.WebSocketHandler):
    def check_origin(self, origin):
        return True

    def open(self):
        if self not in cl:
            cl.append(self)

    def on_close(self):
        if self in cl:
            cl.remove(self)

app = web.Application([
    (r'/ws', SocketHandler),
])

if __name__ == '__main__':
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(8888)
    tornado.ioloop.IOLoop.instance().start()
   
