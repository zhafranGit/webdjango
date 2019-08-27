from django.db import models

# Create your models here.
class Post (models.Model):
    judul = models.CharField(max_length=200)
    # nama = models.CharField(max_length=10)
    body = models.TextField()

    def __str__(self):
        return "{}".format(self.judul)