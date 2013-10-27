from django.db import models

class Tad(models.Model):
    created_time=models.DateTimeField(auto_now_add=True)
    modified_time=models.DateTimeField('last modified',auto_now=True)
    logged_time=models.DateTimeField('last modified',auto_now=True)
    note=models.TextField()
    tags=models.ManyToManyField('Tag')
    
    def __unicode__(self):
        return '%s...%s'%(self.note[:20],self.note[-20:])

class Tag(models.Model):
    name=models.CharField(max_length=50)
    
    def __unicode__(self):
        return self.name