'''
Copyright (c) 2018 Tobias Sommer
Licensed under the MIT License. See LICENSE file in the project root for full license information.
'''
import os
import base64

LOG_PATH = "logfile.log"

APPLICATION_NAME = os.environ.get('APPLICATION_NAME')
SERVER_PORT = os.environ.get('SERVER_PORT')
MICROSERVICE_SUBSCRIPTION_ENABLED = os.environ.get('MICROSERVICE_SUBSCRIPTION_ENABLED')
C8Y_BASEURL = os.environ.get('C8Y_BASEURL')
C8Y_BASEURL_MQTT = os.environ.get('C8Y_BASEURL_MQTT')
C8Y_MICROSERVICE_ISOLATION = os.environ.get('C8Y_MICROSERVICE_ISOLATION')
C8Y_BOOTSTRAP_REGISTER = os.environ.get('C8Y_BOOTSTRAP_REGISTER')
C8Y_BOOTSTRAP_TENANT = os.environ.get('C8Y_BOOTSTRAP_TENANT')
C8Y_BOOTSTRAP_USER = os.environ.get('C8Y_BOOTSTRAP_USER')
C8Y_BOOTSTRAP_PASSWORD = os.environ.get('C8Y_BOOTSTRAP_PASSWORD')
C8Y_TENANT = os.environ.get('C8Y_TENANT')
C8Y_USER = os.environ.get('C8Y_USER')
C8Y_PASSWORD = os.environ.get('C8Y_PASSWORD')
MEMORY_LIMIT = os.environ.get('MEMORY_LIMIT')
PROXY_HTTP_HOST = os.environ.get('PROXY_HTTP_HOST')
PROXY_HTTP_PORT = os.environ.get('PROXY_HTTP_PORT')
PROXY_HTTP_NON_PROXY_HOSTS = os.environ.get('PROXY_HTTP_NON_PROXY_HOSTS')
PROXY_HTTPS_HOST = os.environ.get('PROXY_HTTPS_HOST')
PROXY_HTTPS_PORT = os.environ.get('PROXY_HTTPS_PORT')
PROXY_SOCKS_HOST = os.environ.get('PROXY_SOCKS_HOST')
PROXY_SOCKS_PORT = os.environ.get('PROXY_SOCKS_PORT')

BOOTSTRAP_AUTHENTHICATION_HEADER = 'Basic ' + base64.b64encode((C8Y_BOOTSTRAP_TENANT + '/' + C8Y_BOOTSTRAP_USER + ':' + C8Y_BOOTSTRAP_PASSWORD).encode()).decode()