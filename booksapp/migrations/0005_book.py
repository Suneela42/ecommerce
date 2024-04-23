# Generated by Django 5.0.1 on 2024-03-25 13:13

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("booksapp", "0004_blogs_author"),
    ]

    operations = [
        migrations.CreateModel(
            name="Book",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("book_name", models.CharField(max_length=100)),
                ("seller_name", models.CharField(max_length=100)),
                ("num_books", models.IntegerField()),
                ("price", models.DecimalField(decimal_places=2, max_digits=1000)),
                ("describe", models.CharField(max_length=200)),
                ("stream", models.CharField(max_length=100)),
                ("is_series", models.CharField(max_length=20)),
            ],
        ),
    ]