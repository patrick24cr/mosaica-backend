from django.utils import timezone, dateformat
from django.db import models
from .user import User
from .tile import Tile

class UserTileScore(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tile = models.ForeignKey(Tile, on_delete=models.CASCADE)
    score = models.IntegerField()
    date = models.DateTimeField(default=dateformat.format(timezone.now(), 'Y-m-d H:i:s'), null=True, blank=True)
