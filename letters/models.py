import datetime
from django.db import models

# Create your models here.
from django.utils import timezone

class Author(models.Model):
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name
    
class Letter(models.Model):
    title = models.CharField(max_length=200)
    letter_md = models.CharField(max_length=20000)
    pub_date = models.DateTimeField('date published')
    pub_author = models.ForeignKey(Author, on_delete=models.CASCADE)
    def __str__(self):
        return self.letter_md
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
