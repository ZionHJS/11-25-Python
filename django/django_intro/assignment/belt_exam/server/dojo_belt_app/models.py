from django.db import models
import re

# Create your models here.
class UserManager(models.Manager):
    def basic_validator_user(self, postData):
        errors = {}
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(postData['email']):
            errors['email'] = ("Invalid email address!")
        if len(postData['first_name']) < 2:
            errors['first_name'] = " First Name should be at least 2 characters and letters only!"
        if len(postData['last_name']) <2:
            errors['last_name'] = "Last Name should be at least 2 characters and letters only!"
        if len(postData['password']) < 8:
            errors['password'] = "Password should be at least 8 characters!"
        return errors

class User(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    email = models.CharField(max_length=125)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()

class WishManager(models.Manager):
    def basic_validator_wish(self, postData):
        errors = {}
        if len(postData['wish_name']) < 3:
            errors['wish_name'] = "A wish must consist of at least 3 characters!"
        if len(postData['wish_des']) < 1:
            errors['wish_des'] = "A description must be provided!"
        return errors

class Wish(models.Model):
    wish_name = models.CharField(max_length=45)
    wish_des = models.CharField(max_length=255)
    granted = models.BooleanField(default=False)
    user = models.ForeignKey(User, related_name="wishes", on_delete = models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = WishManager()
