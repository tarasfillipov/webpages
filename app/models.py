from django.db import models
import datetime
class Group(models.Model):
    title = models.CharField(max_length=100, blank=True)
    def __unicode__(self):
        return self.title

class Student(models.Model):
    fullname = models.CharField(max_length=100, blank=True)
    group = models.ForeignKey(Group)

class Lesson(models.Model):
    date = models.DateField()
    title = models.CharField(max_length=100, blank=True)
    teacher = models.CharField(max_length=100, blank=True)
    group = models.ForeignKey(Group)

