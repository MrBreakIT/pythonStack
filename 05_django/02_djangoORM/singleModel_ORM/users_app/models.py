from django.db import models

# Create your models here.
class Users (models.Model):
    # id - is implicit when creating models
    fname = models.CharField(max_length=45)
    lname = models.CharField(max_length=45)
    email = models.EmailField(max_length=255)
    age = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


# this fx formats the result in cmd
# def __repr__(self):
#     return "Title: {}".format(self.title)

















