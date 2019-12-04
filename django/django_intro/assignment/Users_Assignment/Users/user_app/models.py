from django.db import models

# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email_address = models.CharField(max_length=255)
    age = models.IntegerField
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

#create
newUser_neil = User.objects.create(first_name='neil', last_name='D', email_address='neil_D@gmail.com', age=30)
newUser_Rolando = User.objects.create(first_name='Rolando', last_name='Lopantzi', emial_address='rolando@gmail.com', age=27)
nweUser_Adam = User.objects.create(first_name='Adam', last_name='R',email_address='adam@gmail.com', age=30)

#get
all_users = User.objects.all()
first_user = User.objects.first()
last_user = User.objects.last()

#update
name_update = User.objects.get(id=7)
name_update.last_name='pancakes'
name_update.save()

#delete
user_delete = User.objects.get(id=2)
user_delete.delete()

user_all = User.objects.all()
