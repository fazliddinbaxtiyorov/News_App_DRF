from django.db import models


# Create your models here.

class NewsModels(models.Model):
    title = models.CharField(max_length=80)
    link = models.URLField(max_length=100)
    photo = models.URLField(null=True, blank=True)
    content = models.CharField(max_length=100)
    date_time = models.CharField(max_length=10)

    class Meta:
        db_table = 'news.db'
