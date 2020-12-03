from django.db import models
from datetime import datetime
from django.contrib.auth.models import User



class Item(models.Model):
    created_by = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    price = models.IntegerField()
    countInStock = models.IntegerField(default=0)
    is_published = models.BooleanField(default=True)
    list_date = models.DateTimeField(default=datetime.now, blank=True)
    photo_main = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)

    def __str__(self):
        return self.name
