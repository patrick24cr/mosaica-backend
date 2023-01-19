from django.db import models


class User(models.Model):

    uid = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    
