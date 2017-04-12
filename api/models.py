# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

from mongoengine import *


class Address(EmbeddedDocument):
    building = StringField() 
    coord = ListField(IntField(),default=list)
    street = StringField()
    zipcode = StringField()

class Grades(EmbeddedDocument):
    date = DateTimeField() 
    grade = StringField()
    score = IntField()

class Restaurants(Document):
    id = StringField(primary_key=True)
    restaurant_id = StringField()
    address = EmbeddedDocumentField(Address)
    borough = StringField()
    cuisine = StringField()
    grades = ListField(EmbeddedDocumentField(Grades))
    name = StringField()
    meta = {'collection':'restaurants','allow_inheritance' : False}

    def single(self):
        return self.grades[0].score
