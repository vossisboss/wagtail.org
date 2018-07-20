# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-12-01 12:15
from __future__ import unicode_literals

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('developers', '0003_developerspageoptions_icon_new_choices'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='developerspage',
            name='body_heading',
        ),
        migrations.RemoveField(
            model_name='developerspage',
            name='introduction',
        ),
        migrations.AlterField(
            model_name='developerspage',
            name='body',
            field=wagtail.core.fields.StreamField((('code', wagtail.core.blocks.StructBlock((('title', wagtail.core.blocks.CharBlock()), ('subtitle', wagtail.core.blocks.CharBlock(required=False)), ('code', wagtail.core.blocks.StructBlock((('language', wagtail.core.blocks.ChoiceBlock(choices=[('bash', 'Bash/Shell'), ('css', 'CSS'), ('django', 'Django templating language'), ('html', 'HTML'), ('javascript', 'Javascript'), ('python', 'Python'), ('scss', 'SCSS')])), ('code', wagtail.core.blocks.TextBlock())))), ('link', wagtail.core.blocks.StructBlock((('link_text', wagtail.core.blocks.CharBlock()), ('link_text_bold', wagtail.core.blocks.CharBlock(required=False)), ('link_page', wagtail.core.blocks.PageChooserBlock(required=False)), ('link_url', wagtail.core.blocks.CharBlock(required=False)))))), template='developers/blocks/code_with_link_block.html')),)),
        ),
    ]
