from django.db import models
from folders.models import Folder


def get_default_folder():
    """Ensures that a Folder with id=1 exists and returns its ID."""
    folder, created = Folder.objects.get_or_create(id=1, defaults={'name': 'Default Folder'})
    return folder.id
class File(models.Model):
    name = models.CharField(max_length= 100)
    folder = models.ForeignKey(Folder, on_delete= models.CASCADE, default= get_default_folder, related_name= "the_folder_that_contains_the_file")
