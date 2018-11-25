'''
Copyright (c) 2018 Tobias Sommer
Licensed under the MIT License. See LICENSE file in the project root for full license information.
'''
import logging
import base64
import tornado.web
import bootstrap.application as c8y_bootstrap

class C8YBaseHandler(tornado.web.RequestHandler):

    def prepare(self):
        logging.info(self.request.headers)
        credentials = self.request.headers['Authorization']
        self.auth = {
            'request': credentials,
            'service': c8y_bootstrap.get_auth_header(self.__get_tenant(credentials.split(' ', 1)[1]))
        }

    def __get_tenant(self, credentials):
        credentials = base64.b64decode(credentials).decode('utf-8')
        return credentials.split('/', 1)[0]
