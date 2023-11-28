from django.db import models


# Create your models here.

class NewsModels(models.Model):
    title = models.CharField(max_length=80)
    link = models.URLField(max_length=120)
    photo = models.ImageField()
    content = models.CharField(max_length=120)
    date_time = models.CharField(max_length=10)

    class Meta:
        db_table = 'news.db'
