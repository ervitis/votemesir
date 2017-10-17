# -*- coding: utf-8 -*-

from __future__ import print_function

from libs.flask import Flask


def create_app(name):
    return Flask(name)


app = create_app(__name__)


@app.route('/')
def hello():
    return 'hello world'
