'''
Copyright (c) 2018 Tobias Sommer
Licensed under the MIT License. See LICENSE file in the project root for full license information.
'''
import tornado.web
import json

class HealthHandler(tornado.web.RequestHandler):
    def get(self):
        health = {
            'status': 'UP'
        }
        self.set_header('Content-Type', 'application/json')
        self.write(json.dumps(health))
        self.finish()