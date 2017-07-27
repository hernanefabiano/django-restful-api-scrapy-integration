from __future__ import absolute_import, division, print_function, unicode_literals

from mongoengine import *


class News(Document):
    category     = StringField(required=False)
    summary      = StringField(required=False)
    media        = StringField(required=False)
    section      = StringField(required=False)
    url          = StringField(required=False)
    headline     = StringField(required=False)
    datescrapped = StringField(required=False)
