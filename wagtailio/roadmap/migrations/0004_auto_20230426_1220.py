# Generated by Django 3.2.18 on 2023-04-26 12:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("roadmap", "0003_auto_20230426_0914"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="item",
            name="needs_sponsorship",
        ),
    ]