from django.db import models

# Create your models here.


class Blog(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateField(auto_now=True)
    content = models.TextField()
    image = models.ImageField(upload_to='images/')

