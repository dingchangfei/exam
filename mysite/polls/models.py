from django.db import models

# Create your models here.
class Question(models.Model):
    qusertion_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

class Choice(models.Model):
    question = models.ForeignKey(Question)
    choice_text = models.CharField(max_length=200)
    vates = models.IntegerField(default=0)
