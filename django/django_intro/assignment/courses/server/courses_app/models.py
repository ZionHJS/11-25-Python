from __future__ import unicode_literals
from django.db import models

# Create your models here.
class Course(models.Model):
    course_name = models.CharField(max_length=45)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    object = CourseManager()

class CourseManager(models.Manager):
    def basic_validator(self, postData):
        errors={}
        if len(postData['add_name']) < 5:
            errors['add_name'] = 'name should be at least 5 characters'
        if len(postData['add_des']) < 15:
            errors['add_des'] = 'description should be at least 15 characters'
        return errors
