# Generated by Django 3.1.4 on 2020-12-16 03:38

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='date',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='blog',
            name='description',
            field=models.CharField(default=0.000363036303630363, max_length=200),
            preserve_default=False,
        ),
    ]
