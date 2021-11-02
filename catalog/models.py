
from django.db import models
from django.contrib.postgres.fields import ArrayField

# Create your models here.

class Graphs(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=1000)
    x1 = models.IntegerField(help_text="x1")
    x2 = models.IntegerField(help_text="x2")
    x3 = models.IntegerField(help_text="x3")
    x4 = models.IntegerField(help_text="x4")
    x5 = models.IntegerField(help_text="x5")
    y1 = models.IntegerField(help_text="y1")
    y2 = models.IntegerField(help_text="y2")
    y3 = models.IntegerField(help_text="y3")
    y4 = models.IntegerField(help_text="y4")
    y5 = models.IntegerField(help_text="y5")
    def __str__(self):
        return self.title +' '+self.description + ' '
        + self.x1 + ' '+ self.x2  + ' '+ self.x3 + ' '+ self.x4 + ' '+ self.x5 +  ' ' 
        + self.y1 + ' '+ self.y2 + ' '+ self.y3 + ' '+ self.y4 + + self.y5
