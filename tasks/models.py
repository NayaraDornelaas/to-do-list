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