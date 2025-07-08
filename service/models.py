from django.db import models
from django.db import models


class SKILL(models.Model):
    title = models.CharField(max_length=100)
    desc  = models.TextField()


class login(models.Model):
    name=models.CharField(max_length=20)
    email=models.CharField(max_length=30)
    password=models.CharField(max_length=20)

class tweet(models.Model):
    title=models.CharField(max_length=20)
    desc=models.TextField()
    image=models.FileField(upload_to='news/', max_length=200,null=True, default=None)
    
    def __str__(self):
        return self.title  
    
       

    


# Create your models here.
