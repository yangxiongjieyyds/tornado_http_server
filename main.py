# coding:utf-8

import config
from server import routes
from tornado import web, httpserver, ioloop

if __name__ == '__main__':
    config.load_config()
    listen_port = config.conf['server']['port']
    assert listen_port > 1000
    app = web.Application(handlers=routes.routes)
    http_server = httpserver.HTTPServer(app)
    http_server.listen(listen_port)
    ioloop.IOLoop.current().start()
