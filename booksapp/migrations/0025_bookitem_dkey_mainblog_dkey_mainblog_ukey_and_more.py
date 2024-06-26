# Generated by Django 5.0.1 on 2024-04-04 10:30

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("booksapp", "0024_alter_bookitem_image"),
    ]

    operations = [
        migrations.AddField(
            model_name="bookitem",
            name="dkey",
            field=models.CharField(default="book", max_length=220),
        ),
        migrations.AddField(
            model_name="mainblog",
            name="dkey",
            field=models.CharField(default="blog", max_length=220),
        ),
        migrations.AddField(
            model_name="mainblog",
            name="ukey",
            field=models.CharField(default="blog", max_length=200),
        ),
        migrations.AddField(
            model_name="uploadblog",
            name="dkey",
            field=models.CharField(default="blog", max_length=220),
        ),
        migrations.AddField(
            model_name="uploadblog",
            name="ukey",
            field=models.CharField(default="blog", max_length=200),
        ),
    ]
