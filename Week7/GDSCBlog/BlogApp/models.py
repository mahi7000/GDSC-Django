from django.db import models
from django.contrib.postgres.fields import ArrayField

class Post(models.Model):
    title = models.CharField(max_length=255, unique=True)
    content = models.TextField(max_length=1000)
    category = models.CharField(max_length=255)
    image = models.ImageField(upload_to='image/')
    tags = ArrayField(models.CharField(max_length=255), default=list)

    def __str__(self):
        return self.title