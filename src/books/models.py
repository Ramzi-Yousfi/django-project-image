from django.db import models
from datetime import datetime

class Books(models.Model):
    title = models.CharField(max_length=150)
    author = models.CharField(max_length=150)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    pageCount = models.IntegerField()
    published_date = models.DateField(default=datetime.now)
    thumbnail = models.CharField(max_length=256)
        
    