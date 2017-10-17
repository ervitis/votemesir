# -*- coding: utf-8 -*-

from __future__ import absolute_import


def add_third_libraries():
    from google.appengine.ext import vendor

    vendor.add('libs')


add_third_libraries()
