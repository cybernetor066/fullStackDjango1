from django.db import models

# Create your models here.
# A model is the single, definitive source of data about your data. It contains the essential fields and behaviors of the
# data you’re storing. Generally, each model maps to a single database table.
# The basics:
# • Each model is a Python class that subclasses django.db.models.Model.
# • Each attribute of the model represents a database field.
# • With all of this, Django gives you an automatically-generated database-access API; see Making queries.

# Follow these steps:
# • Change your models (in models.py).
# • Run python manage.py makemigrations to create migrations for those changes
# • Run python manage.py migrate to apply those changes to the database.

class Person(models.Model):
    email_address = models.EmailField(max_length=200)
    password = models.CharField(max_length=200)
    nickname = models.CharField(max_length=200)
    # signup_date = models.DateField()


class Users(models.Model):
    email_address = models.EmailField(max_length=200)
    password = models.CharField(max_length=200)
    nickname = models.CharField(max_length=200)
    # signup_date = models.DateField()