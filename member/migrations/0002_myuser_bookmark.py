# Generated by Django 3.1.3 on 2020-11-30 11:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0001_initial'),
        ('member', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='myuser',
            name='bookmark',
            field=models.ManyToManyField(to='post.Post'),
        ),
    ]