
from tornado.websocket import websocket_connect
from tornado import gen
import tornado


#def conn():
#    return websocket_connect('ws://localhost:8888/ws/')


@gen.coroutine
def main():
    try:
        print "Trying"
        blah = yield websocket_connect('ws://localhost:8888/ws/')
        import pdb; pdb.set_trace()
        print "Complete"
    except:
        import pdb; pdb.set_trace()


#io_loop = tornado.ioloop.IOLoop.current()
#io_loop.start()
#io_loop.run_sync(main)

main()
