from django.db import models
import re

# Create your models here.
class UserManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData['first_name']) < 2:
            errors['first_name'] = " First Name should be at least 2 characters and letters only!"
        if len(postData['last_name']) <2:
            errors['last_name'] = "Last Name should be at least 2 characters and letters only!"
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(postData['email']):
            errors['email'] = ("Invalid email address!")
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

class BookManager(models.Manager):
    def basic_validator_book(self, postData):
        errors = {}
        if len(postData['book_title']) < 4:
            errors['book_title'] = " First Name should be at least 4 characters and letters only!"
        if len(postData['book_author']) < 6:
            errors['book_author'] = "author should be at least 6 characters and letters only!"
        return errors

class Book(models.Model):
    title = models.CharField(max_length=55)
    author = models.CharField(max_length=55)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = BookManager()

class ReviewManager(models.Manager):
    def basic_validator_review(self, postData):
        errors = {}
        if len(postData['review_des']) < 12:
            errors['review_des'] = "Review should be at least 12 characters and letters only!"
        return errors

class Review(models.Model):
    description = models.CharField(max_length=255)
    rating = models.IntegerField(default=0)
    user = models.ForeignKey(User, related_name="reviews", on_delete = models.CASCADE)
    book = models.ForeignKey(Book, related_name="reviews", on_delete = models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ReviewManager()