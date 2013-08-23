from django.db import models

class Note(models.Model):

    text = models.TextField(max_length=100, blank=True)
    photo = models.ImageField(upload_to='photos', blank=True, null=True)