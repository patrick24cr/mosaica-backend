from django.db import models


class Tile(models.Model):

    name = models.CharField(max_length=100)
