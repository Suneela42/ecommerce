# Generated by Django 5.0.1 on 2024-04-04 04:58

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("booksapp", "0021_alter_blogs_image"),
    ]

    operations = [
        migrations.AddField(
            model_name="bookitem",
            name="email",
            field=models.EmailField(default="hari@gmail.com.com", max_length=254),
        ),
    ]