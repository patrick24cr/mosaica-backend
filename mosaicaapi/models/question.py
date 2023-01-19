import datetime
from django.db import models
from .user import User
from .tile import Tile
from .responseSet import responseSet

class question(models.Model):

    tile = models.ForeignKey(Tile, on_delete=models.CASCADE)
    english = models.CharField(max_length=1000)
    spanish = models.CharField(max_length=1000)
    aspect1 = models.ForeignKey(responseSet, on_delete=models.CASCADE)
    aspect2 = models.ForeignKey(responseSet, on_delete=models.CASCADE)
    aspect3 = models.ForeignKey(responseSet, on_delete=models.CASCADE)
    aspect4 = models.ForeignKey(responseSet, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name
    
    