from django.db import models

# Create your models here.


class Tag(models.Model):
    name = models.CharField(max_length=255)

    albums = models.ManyToManyField("albums.Album", related_name="tags")
