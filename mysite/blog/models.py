from django.db import models
from django.utils import timezone
# Create your models here.
class Posts(models.Model):
    author = models.CharField(max_length=50, )
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True,null=True,default='enter your description')
    date = models.DateTimeField(default=timezone.now)
    image = models.ImageField(upload_to='images/', default='')