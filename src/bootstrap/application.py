'''
Copyright (c) 2018 Tobias Sommer
Licensed under the MIT License. See LICENSE file in the project root for full license information.
'''
import logging
import base64
import time
import requests

import bootstrap.constants as constants

APPLICATION_SUBSCRIPTIONS = {}

def get_subscriptions():
    logging.debug('Poll for subscriptions')
    response = requests.get(constants.C8Y_BASEURL + '/application/currentApplication/subscriptions', headers={'Authorization': constants.BOOTSTRAP_AUTHENTHICATION_HEADER})
    for subscription in response.json()['users']:
        subscription['header'] = 'Basic ' + base64.b64encode((subscription['tenant'] + '/' + subscription['name'] + ':' + subscription['password']).encode()).decode()
        APPLICATION_SUBSCRIPTIONS[subscription['tenant']] = subscription

def poll_subscriptions():
    logging.debug('Start subscription polling')
    while True:
        get_subscriptions()
        time.sleep(30)

def get_auth_header(tenant):
    return APPLICATION_SUBSCRIPTIONS[tenant]['header']
