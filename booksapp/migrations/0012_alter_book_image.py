# Generated by Django 5.0.1 on 2024-04-03 11:25

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("booksapp", "0011_book_image"),
    ]

    operations = [
        migrations.AlterField(
            model_name="book",
            name="image",
            field=models.ImageField(default="django.jpg", upload_to="proof/"),
        ),
    ]