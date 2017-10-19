#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function
from contextlib import closing

try:
    from urllib.request import urlopen
except ImportError:
    from urllib2 import urlopen

import os
import time

CONSTANT_SLEEP = 15
INCREMENT_SLEEP = 17
MULTIPLIER_SLEEP = 2
N = 3

HTTP_CODES = [
    200, 302
]


def get_host_variable():
    try:
        return os.environ['HOST_APPENGINE']
    except KeyError:
        return None


def get_url_variable():
    try:
        return os.environ['URL_PING']
    except KeyError:
        return None


def build_appengine_host(host_name, url):
    assert isinstance(host_name, str) is True
    assert isinstance(url, str) is True

    return 'https://{host}.appspot.com/{url}'.format(host=host_name, url=url)


def change_time_to_sleep(time_to_sleep):
    time_to_sleep += (INCREMENT_SLEEP * MULTIPLIER_SLEEP)
    return time_to_sleep


def main():
    host = get_host_variable()
    url = get_url_variable()
    if host is None or url is None:
        raise Exception('HOST or URL_PING variable is empty')

    time_to_sleep = CONSTANT_SLEEP
    c = 0
    url = build_appengine_host(host, url)

    while c < N:
        try:
            with closing(urlopen(url)) as response:
                assert int(response.code) in HTTP_CODES
                break
        except Exception as e:
            print('{}'.format(e))
            time.sleep(time_to_sleep)
            time_to_sleep = change_time_to_sleep(time_to_sleep)
            c += 1

    if c >= N:
        raise Exception('Something happened with your connection trying to ping {}'.format(url))

    print('Test passed!')


if __name__ == '__main__':
    main()
