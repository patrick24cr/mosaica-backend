from django.db import models
from .user import User
from .tile import Tile

class UserTileScore(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tile = models.ForeignKey(Tile, on_delete=models.CASCADE)
    score = models.IntegerField()
    date = models.DateField(auto_now=True)
