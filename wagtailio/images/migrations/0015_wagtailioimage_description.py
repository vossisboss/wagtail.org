# Generated by Django 5.0.9 on 2024-10-30 20:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("images", "0014_alter_wagtailiorendition_file"),
    ]

    operations = [
        migrations.AddField(
            model_name="wagtailioimage",
            name="description",
            field=models.CharField(
                blank=True, default="", max_length=255, verbose_name="description"
            ),
        ),
    ]