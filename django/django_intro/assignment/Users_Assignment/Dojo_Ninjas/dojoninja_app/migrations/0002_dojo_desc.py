# Generated by Django 2.2 on 2019-12-05 01:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dojoninja_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='dojo',
            name='desc',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
    ]
