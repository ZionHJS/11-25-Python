from django.db import models
import re

# Create your models here.
class UserManager(models.Manager):
    def basic_validator(self, postData):
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

    def basic_validator_info(self, postData):
        errors = {}
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(postData['update_email']):
            errors['update_email'] = ("Invalid email address!")
        if len(postData['update_first_name']) < 2:
            errors['update_first_name'] = " First Name should be at least 2 characters and letters only!"
        if len(postData['update_last_name']) <2:
            errors['update_last_name'] = "Last Name should be at least 2 characters and letters only!"
        return errors

    def basic_validator_password(self, postData):
        errors = {}
        if len(postData['update_password']) < 8:
            errors['update_password'] = "Password should be at least 8 characters!"
        return errors

class User(models.Model):
    email = models.CharField(max_length=125)
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    password = models.CharField(max_length=255)
    description = models.CharField(max_length=255, default="default description")
    user_level = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()

class MessageManager(models.Manager):
    def basic_validator_message(self, postData):
        errors = {}
        if len(postData['message_content']) < 4:
            errors['message_content'] = " Message should be at least 4 characters and letters only!"
        return errors

class Message(models.Model):
    content = models.CharField(max_length=255)
    msg_author = models.ForeignKey(User, related_name="messages_wrote", on_delete = models.CASCADE)
    msg_owner = models.ForeignKey(User, related_name="messages_own", on_delete = models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = MessageManager()

class CommentManager(models.Manager):
    def basic_validator_comment(self, postData):
        errors = {}
        if len(postData['comment_content']) < 4:
            errors['comment_content'] = " Comment should be at least 4 characters and letters only!"
        return errors

class Comment(models.Model):
    content = models.CharField(max_length=255)
    user = models.ForeignKey(User, related_name="comments", on_delete = models.CASCADE)
    message = models.ForeignKey(Message, related_name="comments", on_delete = models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = CommentManager()
