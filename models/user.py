# -*- coding: utf-8 -*-

from google.appengine.ext import ndb
import yaml

class ModelUser(ndb.Model):
    email = ndb.StringProperty()
    url_email_validation = ndb.StringProperty()
    date_last_vote = ndb.DateTimeProperty()
    password = ndb.StringProperty()
    name = ndb.StringProperty()
    surname = ndb.StringProperty()
