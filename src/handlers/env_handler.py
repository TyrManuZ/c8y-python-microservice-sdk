'''
Copyright (c) 2018 Tobias Sommer
Licensed under the MIT License. See LICENSE file in the project root for full license information.
'''
import tornado.web
import json
import os

import bootstrap.constants as constants

from handlers.base_handler import C8YBaseHandler

class EnvironmentVariablesHandler(C8YBaseHandler):
    def get(self):
        environment = {
            'APPLICATION_NAME': constants.APPLICATION_NAME,
            'SERVER_PORT': constants.SERVER_PORT,
            'MICROSERVICE_SUBSCRIPTION_ENABLED': constants.MICROSERVICE_SUBSCRIPTION_ENABLED,
            'C8Y_BASEURL': constants.C8Y_BASEURL,
            'C8Y_BASEURL_MQTT': constants.C8Y_BASEURL_MQTT,
            'C8Y_MICROSERVICE_ISOLATION': constants.C8Y_MICROSERVICE_ISOLATION,
            'C8Y_BOOTSTRAP_REGISTER': constants.C8Y_BOOTSTRAP_REGISTER,
            'C8Y_BOOTSTRAP_TENANT': constants.C8Y_BOOTSTRAP_TENANT,
            'C8Y_BOOTSTRAP_USER': constants.C8Y_BOOTSTRAP_USER,
            'C8Y_BOOTSTRAP_PASSWORD': constants.C8Y_BOOTSTRAP_PASSWORD,
            'C8Y_TENANT': constants.C8Y_TENANT,
            'C8Y_USER': constants.C8Y_USER,
            'C8Y_PASSWORD': constants.C8Y_PASSWORD,
            'MEMORY_LIMIT': constants.MEMORY_LIMIT,
            'PROXY_HTTP_HOST': constants.PROXY_HTTP_HOST,
            'PROXY_HTTP_PORT': constants.PROXY_HTTP_PORT,
            'PROXY_HTTP_NON_PROXY_HOSTS': constants.PROXY_HTTP_NON_PROXY_HOSTS,
            'PROXY_HTTPS_HOST': constants.PROXY_HTTPS_HOST,
            'PROXY_HTTPS_PORT': constants.PROXY_HTTPS_PORT,
            'PROXY_SOCKS_HOST': constants.PROXY_SOCKS_HOST,
            'PROXY_SOCKS_PORT': constants.PROXY_SOCKS_PORT
        }
        self.set_header('Content-Type', 'application/json')
        self.write(json.dumps(environment))
        self.finish()
