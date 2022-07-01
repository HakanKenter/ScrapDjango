from django.db import models

# Create your models here.
class Annonce(models.Model):
    title=models.CharField(max_length=100)
    photo=models.CharField(max_length=500)
    description=models.CharField(max_length=1000)
    prix=models.CharField(max_length=50)
    date_ajout=models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering=['-date_ajout']
        
    def __str__(self):
        return self.title