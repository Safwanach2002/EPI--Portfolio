from django.db import models

# Create your models here.
class ContentE(models.Model):
    title=models.CharField(max_length=555)
    description=models.TextField()
    video=models.FileField(upload_to='videos/',blank=True,null=True)
    image=models.FileField(upload_to='images/',blank=True,null=True)
    craeted_at=models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title

class ContentM(models.Model):
    title=models.CharField(max_length=555)
    description=models.TextField()
    video=models.FileField(upload_to='videos/',blank=True,null=True)
    image=models.FileField(upload_to='images/',blank=True,null=True)
    craeted_at=models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title
