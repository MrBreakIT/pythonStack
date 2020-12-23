from django.db import models

# Create your models here.
class Dojos (models.Model):
    # id - is implicit when creating models
    name = models.CharField(max_length=45)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=2)
    desc = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return f"{self.name} ({self.city}, {self.state})\n"

class Ninjas (models.Model):
    # id - is implicit when creating models        
    dojo_id = models.ForeignKey(
        Dojos, related_name="ninjas", on_delete=models.CASCADE)
    fname = models.CharField(max_length=45)
    lname = models.CharField(max_length=45)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return f"{self.fname} {self.lname}, {self.dojo_id}\n"

