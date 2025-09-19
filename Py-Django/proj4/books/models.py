from django.db import models

class Book(models.Model):
    # col name
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    published_date = models.DateField()
    isbn = models.CharField(max_length=12, unique=True)

def __str__(self):
    return self.title