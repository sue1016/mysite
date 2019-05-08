import datetime
from django.db import models

# Create your models here.
from django.utils import timezone
# models.py

from solo.models import SingletonModel


class ChatBot(SingletonModel):
    name = models.CharField(max_length=255, default='Cara Sue')


    def __unicode__(self):
        return u"ChatBot"

    class Meta:
        verbose_name = "ChatBot"
        
class Author(models.Model):
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name
    
class Letter(models.Model):
    title = models.CharField(max_length=200)
    letter_md = models.CharField(max_length=20000)
    pub_date = models.DateTimeField('date published')
    pub_author = models.ForeignKey(Author, on_delete=models.CASCADE)
    hasDeleted = models.BooleanField(default=False)
    def __str__(self):
        return self.letter_md
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class Todo(models.Model):
    content = models.CharField(max_length=20000)
    plan_md = models.CharField(max_length=20000,blank=True)
    pub_date = models.DateTimeField('date published')
    hasChecked = models.BooleanField()
    check_date = models.DateTimeField('date checked',blank=True)
    hasDeleted = models.BooleanField(default=False)