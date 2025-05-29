from django.db import models
from django.utils import timezone

# Create your models here.

class Post (models.Model):
    #author= models.ManyToManyField()
    #img
    title = models.CharField(max_length= 255)
    content = models.TextField()
    #category = models.
    #tag
    counted_view = models.IntegerField(default=0)
    status = models.BooleanField(default=False)
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(null=True)
    update_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['-created_date']
    