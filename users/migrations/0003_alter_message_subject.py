# Generated by Django 5.0.7 on 2024-07-22 12:51

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0002_message"),
    ]

    operations = [
        migrations.AlterField(
            model_name="message",
            name="subject",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT, to="users.profile"
            ),
        ),
    ]
