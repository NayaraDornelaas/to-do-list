from django.db import models

# Create your models here.
##################################################################################################
""" A model is the single, definitive source of information about your data. 
It contains the essential fields and behaviors of the data you're storing. 
Generally, each model maps to a single database table. 

The basics: -Each model is a Python class that subclasses django.db.models.Model;
.-Each attribute of the model represents a database field."""
###################################################################################################

class Task(models.Model):
    title = models.CharField(max_length=200)
    complete = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
# whenever you code up a new model you also generate a migration
# the migration is to create the necessary table in the database (create database tables without writing any SQL (but it can do more))
# comand to prepare the database: python manage.py makemigrations
# to actually migrate it: python manage.py migrate
#if you go straight to the admin panel you won't see the table yet, so it's necessary to register it first at admin.py
