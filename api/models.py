from django.db import models


# Create your models here.

class NewsModels(models.Model):
    title = models.CharField(max_length=200)
    link = models.URLField(max_length=200)
    photo = models.URLField(max_length=200, null=True, blank=True)
    content = models.CharField(max_length=200)
    date_time = models.CharField(max_length=200)

    class Meta:
        db_table = 'news.db'
