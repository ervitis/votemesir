# -*- coding: utf-8 -*-

from google.appengine.ext import db


class ModelUser(db.Model):
    email = db.StringProperty()
    url_email_validation = db.StringProperty()
    date_last_vote = db.DateTimeProperty()
    password = db.StringProperty()
    name = db.StringProperty()
    surname = db.StringProperty()


EMAIL_ADDRESS = '@votemesir.appspotmail.com'
MIN = 6
MAX = 16


def generate_data(n):
    assert (isinstance(n, int) is True and 0 < n < 1001)
    password_prefix = 'Ab_Cd_'

    def generate_word():
        import random
        import string

        vowels = 'aeiou'
        consonants = ''.join(set(string.ascii_lowercase) - set(vowels))

        w = ''
        for i in range(random.choice(range(MIN, MAX))):
            if i % 2 == 0:
                w += random.choice(vowels)
            elif i % 5 == 0:
                w += random.choice(consonants) * 2
            else:
                w += random.choice(consonants)
        return w

    ldata = []
    for _ in range(n):
        m = {
            'email': generate_word() + EMAIL_ADDRESS,
            'url_email_validation': '',
            'date_last_vote': None,
            'password': password_prefix + generate_word(),
            'name': generate_word(),
            'surname': generate_word()
        }
        ldata.append(m)

    return ldata
