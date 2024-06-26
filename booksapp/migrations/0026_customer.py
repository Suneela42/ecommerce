# Generated by Django 5.0.1 on 2024-04-05 04:53

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("booksapp", "0025_bookitem_dkey_mainblog_dkey_mainblog_ukey_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="Customer",
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
                ("full_name", models.CharField(max_length=100)),
                ("address_line1", models.CharField(max_length=255)),
                ("city", models.CharField(max_length=100)),
                ("state", models.CharField(max_length=100)),
                ("postal_code", models.CharField(max_length=20)),
                ("country", models.CharField(max_length=100)),
            ],
        ),
    ]
