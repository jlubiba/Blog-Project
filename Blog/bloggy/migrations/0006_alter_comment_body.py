# Generated by Django 5.1.5 on 2025-01-27 11:56

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("bloggy", "0005_comment"),
    ]

    operations = [
        migrations.AlterField(
            model_name="comment",
            name="body",
            field=models.TextField(verbose_name="Comment..."),
        ),
    ]
