from django.db import models
from .responseSet import ResponseSet
from .tile import Tile

class Question(models.Model):

    tile = models.ForeignKey(Tile, on_delete=models.CASCADE)
    english = models.CharField(max_length=1000)
    spanish = models.CharField(max_length=1000)
    aspect1 = models.ForeignKey(ResponseSet, null=True, related_name='aspect1', on_delete=models.CASCADE)
    aspect2 = models.ForeignKey(ResponseSet, null=True, related_name='aspect2', on_delete=models.CASCADE)
    aspect3 = models.ForeignKey(ResponseSet, null=True, related_name='aspect3', on_delete=models.CASCADE)
    aspect4 = models.ForeignKey(ResponseSet, null=True, related_name='aspect4', on_delete=models.CASCADE)
