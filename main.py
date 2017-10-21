# -*- coding: utf-8 -*-

from __future__ import print_function

import logging
from libs.flask import Flask, request


def create_app(name):
    return Flask(name)


app = create_app(__name__)


@app.route('/ping')
def hello():
    return 'hello world'


@app.route('/_ah/mail', methods=['POST'])
def receiver_handler_email():
    logging.info("Received a message from: " + request.form)
