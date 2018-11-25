'''
Copyright (c) 2018 Tobias Sommer
Licensed under the MIT License. See LICENSE file in the project root for full license information.
'''
import logging
import subprocess
import io

from handlers.base_handler import C8YBaseHandler

class LogHandler(C8YBaseHandler):
    def initialize(self, logpath):
        self.logpath = logpath

    def get(self):
        logging.debug('Get log')
        lines = self.get_argument('lines', default=100, strip=True)
        proc = subprocess.Popen(['tail', '-' + str(lines), self.logpath], stdout=subprocess.PIPE)
        for line in io.TextIOWrapper(proc.stdout, encoding="utf-8"):
            self.write(line)
        self.finish()
        