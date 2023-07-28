from django.db import models

# Create your models here.


class Books(models.Model):
    title = models.CharField(max_length=120)
    body = models.TextField()
    author = models.CharField(max_length=150, blank=True, null=True)
    isbn = models.CharField(max_length=12)
    janr = models.CharField(max_length=120)
    narxi = models.CharField(max_length=12, null=True, blank=True)


    def __str__(self):
        return self.title