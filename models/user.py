# -*- coding: utf-8 -*-

from google.appengine.ext import ndb


class ModelUser(ndb.Model):
    email = ndb.StringProperty()
    url_email_validation = ndb.StringProperty()
    date_last_vote = ndb.DateTimeProperty()
    password = ndb.StringProperty()
    name = ndb.StringProperty()
    surname = ndb.StringProperty()


def generate_data(n):
    assert (isinstance(n, int) is True and 0 < n < 1001)
    password_prefix = 'Ab_Cd_'

    def generate_word():
        import random
        import string

        vowels = 'aeiou'
        consonants = ''.join(set(string.ascii_lowercase) - set(vowels))

        w = ''
        for i in range(random.choice(range(7, 12))):
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
            'email': generate_word() + '@votemesir.appspotmail.com',
            'url_email_validation': '',
            'date_last_vote': None,
            'password': password_prefix + generate_word(),
            'name': generate_word(),
            'surname': generate_word()
        }
        ldata.append(m)

    return ldata
