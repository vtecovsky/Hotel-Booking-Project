# Generated by Django 4.2.7 on 2023-11-11 21:38

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("hotels", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="hotel",
            name="reviews",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="hotels.review",
            ),
        ),
    ]
