#!python
# -*- coding: UTF-8 -*-

'''
Package initialization.
'''

import tornado.ioloop
import tornado.web

__pyver__ = ['3.2.3']
__created__ = ['6.7.2012']
__authors__ = ['Toby <codenamekt@gmail.com>']
__copyright__ = ['GNU GPL v3 <http://www.gnu.org/licenses/gpl.html>']
__shortdoc__ = 'Package initialization.'


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world")

application = tornado.web.Application([
    (r"/", MainHandler),
])

if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()
