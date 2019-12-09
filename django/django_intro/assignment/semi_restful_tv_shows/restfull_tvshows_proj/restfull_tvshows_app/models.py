from __future__ import unicode_literals
from django.db import models
from datetime import datetime

# Create your models here.
class ShowManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData['add_title']) <= 2:
            errors['add_title'] = 'Title name needs be at least 2 characters'
        if len(postData['add_network']) <= 3:
            errors['add_network'] = 'Network needs be at least 2 characters'
        if len(postData['add_des']) <= 10 and len(postData['add_des']) > 0:
            errors['add_des'] = 'Description needs be at least 10 characters'
        nowtime = datetime.now()
        if nowtime <= datetime.strptime(postData['add_date'], '%Y-%m-%d'):
            errors['add_date'] = 'Date-time needs be in the past'
        return errors

    def basic_update_validator(self, postData):
        errors = {}
        if len(postData['update_title']) <= 2:
            errors['updaet_title'] = 'Title name needs be at least 2 characters'
        if len(postData['update_network']) <= 3:
            errors['update_network'] = 'Network needs be at least 2 characters'
        if len(postData['update_des']) <= 10 and len(postData['update_des']) > 0:
            errors['update_des'] = 'Description needs be at least 10 characters'
        nowtime = datetime.now()
        if postData['update_date']:
            if nowtime <= datetime.strptime(postData['update_date'], '%Y-%m-%d'):
                errors['update_date'] = 'Date-time needs be in the past'
        return errors

class Show(models.Model):
    title = models.CharField(max_length=45)
    network = models.CharField(max_length=45)
    release_date = models.CharField(max_length=45)
    description = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ShowManager()   #add this line 
