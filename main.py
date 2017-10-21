# -*- coding: utf-8 -*-

from __future__ import print_function

import logging
from libs.flask import Flask


def create_app(name):
    return Flask(name)


app = create_app(__name__)


@app.route('/ping')
def hello():
    return 'hello world'


@app.route('/_ah/mail', methods=['POST'])
def receiver_handler_email(mail_message):
    logging.info("Received a message from: " + mail_message.sender)
    plaintext_bodies = mail_message.bodies('text/plain')
    html_bodies = mail_message.bodies('text/html')

    for content_type, body in html_bodies:
        decoded_html = body.decode()
        logging.info("Html body of length %d.", len(decoded_html))
    for content_type, body in plaintext_bodies:
        plaintext = body.decode()
        logging.info("Plain text body of length %d.", len(plaintext))
