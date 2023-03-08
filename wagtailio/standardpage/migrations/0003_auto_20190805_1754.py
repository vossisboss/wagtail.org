# Generated by Django 2.0.13 on 2019-08-05 17:54

from django.db import migrations

import wagtail.blocks
import wagtail.documents.blocks
import wagtail.embeds.blocks
import wagtail.fields
import wagtail.images.blocks

import wagtailio.utils.blocks


class Migration(migrations.Migration):
    dependencies = [
        ("standardpage", "0002_auto_20160728_0925"),
    ]

    operations = [
        migrations.AlterField(
            model_name="standardpage",
            name="body",
            field=wagtail.fields.StreamField(
                [
                    (
                        "h2",
                        wagtail.blocks.CharBlock(classname="title", icon="title"),
                    ),
                    (
                        "h3",
                        wagtail.blocks.CharBlock(classname="title", icon="title"),
                    ),
                    (
                        "h4",
                        wagtail.blocks.CharBlock(classname="title", icon="title"),
                    ),
                    ("intro", wagtail.blocks.RichTextBlock(icon="pilcrow")),
                    ("paragraph", wagtail.blocks.RichTextBlock(icon="pilcrow")),
                    (
                        "blockquote",
                        wagtail.blocks.CharBlock(classname="title", icon="openquote"),
                    ),
                    ("image", wagtail.images.blocks.ImageChooserBlock(icon="image")),
                    (
                        "document",
                        wagtail.documents.blocks.DocumentChooserBlock(
                            icon="doc-full-inverse"
                        ),
                    ),
                    (
                        "imagecaption",
                        wagtail.blocks.StructBlock(
                            [
                                ("image", wagtail.images.blocks.ImageChooserBlock()),
                                ("caption", wagtail.blocks.RichTextBlock()),
                            ],
                            label="Image caption",
                        ),
                    ),
                    (
                        "textimage",
                        wagtail.blocks.StructBlock(
                            [
                                ("text", wagtail.blocks.RichTextBlock()),
                                ("image", wagtail.images.blocks.ImageChooserBlock()),
                                (
                                    "background",
                                    wagtailio.utils.blocks.BackgroundColourChoiceBlock(),
                                ),
                                (
                                    "alignment",
                                    wagtailio.utils.blocks.SimpleImageFormatChoiceBlock(),
                                ),
                            ],
                            icon="image",
                        ),
                    ),
                    (
                        "colourtext",
                        wagtail.blocks.StructBlock(
                            [
                                ("text", wagtail.blocks.RichTextBlock()),
                                (
                                    "background",
                                    wagtailio.utils.blocks.BackgroundColourChoiceBlock(),
                                ),
                            ],
                            icon="pilcrow",
                        ),
                    ),
                    (
                        "calltoaction",
                        wagtail.blocks.StructBlock(
                            [
                                ("text", wagtail.blocks.RichTextBlock()),
                                (
                                    "background",
                                    wagtailio.utils.blocks.BackgroundColourChoiceBlock(),
                                ),
                            ],
                            icon="pilcrow",
                        ),
                    ),
                    (
                        "tripleimage",
                        wagtail.blocks.StructBlock(
                            [
                                (
                                    "first_image",
                                    wagtail.images.blocks.ImageChooserBlock(),
                                ),
                                (
                                    "second_image",
                                    wagtail.images.blocks.ImageChooserBlock(),
                                ),
                                (
                                    "third_image",
                                    wagtail.images.blocks.ImageChooserBlock(),
                                ),
                            ],
                            icon="image",
                        ),
                    ),
                    (
                        "stats",
                        wagtail.blocks.ListBlock(
                            wagtail.blocks.StructBlock(
                                [
                                    (
                                        "image",
                                        wagtail.images.blocks.ImageChooserBlock(),
                                    ),
                                    ("stat", wagtail.blocks.CharBlock()),
                                    ("text", wagtail.blocks.CharBlock()),
                                ],
                                icon="code",
                            )
                        ),
                    ),
                    ("embed", wagtail.embeds.blocks.EmbedBlock(icon="code")),
                    ("markdown", wagtailio.utils.blocks.MarkDownBlock()),
                    (
                        "codeblock",
                        wagtail.blocks.StructBlock(
                            [
                                (
                                    "language",
                                    wagtail.blocks.ChoiceBlock(
                                        choices=[
                                            ("bash", "Bash/Shell"),
                                            ("css", "CSS"),
                                            ("django", "Django templating language"),
                                            ("html", "HTML"),
                                            ("javascript", "Javascript"),
                                            ("python", "Python"),
                                            ("scss", "SCSS"),
                                        ]
                                    ),
                                ),
                                ("code", wagtail.blocks.TextBlock()),
                            ]
                        ),
                    ),
                    (
                        "backers",
                        wagtail.blocks.StructBlock(
                            [
                                (
                                    "gold_backers",
                                    wagtail.blocks.ListBlock(
                                        wagtail.blocks.StructBlock(
                                            [
                                                (
                                                    "name",
                                                    wagtail.blocks.CharBlock(),
                                                ),
                                                (
                                                    "image",
                                                    wagtail.images.blocks.ImageChooserBlock(
                                                        required=False
                                                    ),
                                                ),
                                                (
                                                    "url",
                                                    wagtail.blocks.URLBlock(
                                                        required=False
                                                    ),
                                                ),
                                            ]
                                        )
                                    ),
                                ),
                                (
                                    "silver_backers",
                                    wagtail.blocks.ListBlock(
                                        wagtail.blocks.StructBlock(
                                            [
                                                (
                                                    "name",
                                                    wagtail.blocks.CharBlock(),
                                                ),
                                                (
                                                    "image",
                                                    wagtail.images.blocks.ImageChooserBlock(
                                                        required=False
                                                    ),
                                                ),
                                                (
                                                    "url",
                                                    wagtail.blocks.URLBlock(
                                                        required=False
                                                    ),
                                                ),
                                            ]
                                        )
                                    ),
                                ),
                                (
                                    "bronze_backers",
                                    wagtail.blocks.ListBlock(
                                        wagtail.blocks.StructBlock(
                                            [
                                                (
                                                    "name",
                                                    wagtail.blocks.CharBlock(),
                                                ),
                                                (
                                                    "image",
                                                    wagtail.images.blocks.ImageChooserBlock(
                                                        required=False
                                                    ),
                                                ),
                                                (
                                                    "url",
                                                    wagtail.blocks.URLBlock(
                                                        required=False
                                                    ),
                                                ),
                                            ]
                                        )
                                    ),
                                ),
                                (
                                    "linked_backers",
                                    wagtail.blocks.ListBlock(
                                        wagtail.blocks.StructBlock(
                                            [
                                                (
                                                    "name",
                                                    wagtail.blocks.CharBlock(),
                                                ),
                                                (
                                                    "url",
                                                    wagtail.blocks.URLBlock(
                                                        required=False
                                                    ),
                                                ),
                                            ]
                                        )
                                    ),
                                ),
                                (
                                    "named_backers",
                                    wagtail.blocks.ListBlock(
                                        wagtail.blocks.StructBlock(
                                            [("name", wagtail.blocks.CharBlock())]
                                        )
                                    ),
                                ),
                            ]
                        ),
                    ),
                ]
            ),
        ),
    ]
