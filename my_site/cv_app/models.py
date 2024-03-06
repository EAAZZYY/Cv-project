from django.db import models

# Create your models here.

class Detail(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=100)
    address = models.CharField(max_length=400)
    about_you = models.TextField()
    skills = models.CharField(max_length=200)
    previous_work = models.TextField()
    
    def __str__(self):
        return f'{self.name} cv'