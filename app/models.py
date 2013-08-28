from django.db import models


class Note(models.Model):
    text = models.TextField(max_length=100, blank=True)
    photo = models.ImageField(upload_to='photos', blank=True, null=True)

    def __unicode__(self):
        return self.text


class Book(models.Model):
    title = models.CharField(max_length=50, blank=True)
    notes = models.ManyToManyField(Note)

    def __unicode__(self):
        return self.title
