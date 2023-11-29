from django.db import models


# Create your models here.

class NewsModels(models.Model):
    title = models.CharField(max_length=2000)
    link = models.URLField(max_length=2000)
    photo = models.URLField(max_length=2000, null=True, blank=True)
    content = models.CharField(max_length=2000)
    date_time = models.CharField(max_length=2000)

    class Meta:
        db_table = 'news.db'
