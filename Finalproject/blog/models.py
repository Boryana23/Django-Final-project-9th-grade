from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=50)
    text = models.TextField()
    image = models.ImageField(upload_to="images/")
    time_created = models.DateTimeField(auto_now_add=True)