'''
Copyright (c) 2018 Tobias Sommer
Licensed under the MIT License. See LICENSE file in the project root for full license information.
'''
import logging
import tornado.ioloop
import tornado.web

from handlers.base_handler import C8YBaseHandler

class KillHandler(C8YBaseHandler):
    def get(self):
        logging.debug('Kill webserver')
        tornado.ioloop.IOLoop.current().stop()
