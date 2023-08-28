from django.db import models
from  django.contrib.auth.models import User
# Create your models here.
from datetime import datetime

class Post(models.Model):
    topic = models.CharField(max_length=30)
    title = models.CharField(max_length=40)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    poster = models.ImageField(upload_to='images/',blank=True, null=True)
    description = models.TextField(max_length=300)
    created_date = models.DateTimeField(default=datetime.now)
     

class Like(models.Model):
    post = models.ManyToManyField(Post)
    user = models.ManyToManyField(User)
    created_date = models.DateTimeField(default=datetime.now)

class Comment(models.Model):
    post = models.ManyToManyField(Post)
    user = models.ManyToManyField(User)
    comment = models.TextField(max_length=300)
    created_date = models.DateTimeField(default=datetime.now)
