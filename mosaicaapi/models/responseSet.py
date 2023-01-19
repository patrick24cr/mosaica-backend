from django.db import models

class responseSet(models.Model):

    optionCorrect = models.CharField(max_length=1000)
    option2 = models.CharField(max_length=1000)
    option3 = models.CharField(max_length=1000)
    option4 = models.CharField(max_length=1000)
    
    def __str__(self):
        return self.name
    
    