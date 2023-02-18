import datetime

from django.db import models
from django.utils import timezone

# Create your models here.
class Category(models.Model):
    c_name = models.CharField(max_length=50)
    

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

    def __str__(self):
        return self.c_name

class Task(models.Model):
    # category = models.ForeignKey(Category, on_delete=models.CASCADE)
    # taskID = 
    task_name = models.CharField(max_length=100)
    completed = models.BooleanField(default=False)
    p_date = models.DateTimeField(max_length=200)

    def __str__(self):
        return self.task_name


