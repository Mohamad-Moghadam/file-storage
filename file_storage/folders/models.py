from django.db import models

class Folder(models.Model):
    name = models.CharField(max_length= 100)