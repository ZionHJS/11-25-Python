from django.db import models

# Create your models here.
class Show(models.Model):
    title = models.CharField(max_length=45)
    network = models.CharField(max_length=45)
    release_date = models.CharField(max_length=45)
    description = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ShowManager()

class ShowManager(models.manager):
    def basic_validator(self, postData):
        errors:{}
        if len(postData.title) < 2:
            errors['name'] = 'Title name needs be at least 2 characters'
