# Generated by Django 4.2 on 2023-11-27 17:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newsmodels',
            name='link',
            field=models.CharField(max_length=120),
        ),
        migrations.AlterField(
            model_name='newsmodels',
            name='photo',
            field=models.CharField(max_length=300),
        ),
    ]
