'''
Copyright (c) 2018 Tobias Sommer
Licensed under the MIT License. See LICENSE file in the project root for full license information.
'''
import asyncio
import sys
import logging

from logging.handlers import RotatingFileHandler

import tornado.ioloop
import tornado.web

from bootstrap.constants import LOG_PATH
import bootstrap.application as c8y_bootstrap

from handlers.kill_handler import KillHandler
from handlers.log_handler import LogHandler
from handlers.health_handler import HealthHandler
from handlers.env_handler import EnvironmentVariablesHandler



LOG_FORMATTER = logging.Formatter("%(asctime)s [%(threadName)-12.12s] [%(levelname)-5.5s]  %(message)s")

LOGGER = logging.getLogger()
LOGGER.setLevel(logging.DEBUG)
FILE_HANDLER = RotatingFileHandler(LOG_PATH, maxBytes=50*1024*1024)
FILE_HANDLER.setFormatter(LOG_FORMATTER)
CONSOLE_HANDLER = logging.StreamHandler(sys.stdout)
CONSOLE_HANDLER.setFormatter(LOG_FORMATTER)
LOGGER.addHandler(FILE_HANDLER)
LOGGER.addHandler(CONSOLE_HANDLER)

def generateApp():
    return tornado.web.Application([
        (r"/health", HealthHandler),
        (r"/kill", KillHandler),
        (r"/log", LogHandler, dict(logpath=LOG_PATH)),
        (r"/environment", EnvironmentVariablesHandler),
    ])

logging.info('Starting ...')
LOOP = asyncio.get_event_loop()
LOOP.run_in_executor(None, c8y_bootstrap.poll_subscriptions)

logging.info('Service App ...')
APP = generateApp()
APP.listen(80)
tornado.ioloop.IOLoop.current().start()
