# Generated by Django 3.2.12 on 2022-08-31 16:29

from django.db import migrations

import wagtail.core.blocks
import wagtail.core.fields
import wagtail.documents.blocks
import wagtail.embeds.blocks
import wagtail.images.blocks

import wagtailio.utils.blocks


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0008_featuredpost"),
    ]

    operations = [
        migrations.AlterField(
            model_name="blogpage",
            name="body",
            field=wagtail.core.fields.StreamField(
                [
                    (
                        "h2",
                        wagtail.core.blocks.CharBlock(
                            form_classname="title",
                            icon="title",
                            template="patterns/components/streamfields/headings/heading-2.html",
                        ),
                    ),
                    (
                        "h3",
                        wagtail.core.blocks.CharBlock(
                            form_classname="title",
                            icon="title",
                            template="patterns/components/streamfields/headings/heading-3.html",
                        ),
                    ),
                    (
                        "h4",
                        wagtail.core.blocks.CharBlock(
                            form_classname="title",
                            icon="title",
                            template="patterns/components/streamfields/headings/heading-4.html",
                        ),
                    ),
                    (
                        "intro",
                        wagtail.core.blocks.RichTextBlock(
                            icon="pilcrow",
                            template="patterns/components/streamfields/rich_text_block/rich_text_block.html",
                        ),
                    ),
                    (
                        "paragraph",
                        wagtail.core.blocks.RichTextBlock(
                            icon="pilcrow",
                            template="patterns/components/streamfields/rich_text_block/rich_text_block.html",
                        ),
                    ),
                    (
                        "blockquote",
                        wagtail.core.blocks.CharBlock(
                            form_classname="title",
                            icon="openquote",
                            template="patterns/components/streamfields/quotes/standalone_quote_block.html",
                        ),
                    ),
                    (
                        "image",
                        wagtail.images.blocks.ImageChooserBlock(
                            icon="image",
                            template="patterns/components/streamfields/image/image.html",
                        ),
                    ),
                    (
                        "document",
                        wagtail.documents.blocks.DocumentChooserBlock(
                            icon="doc-full-inverse",
                            template="patterns/components/streamfields/document/document.html",
                        ),
                    ),
                    (
                        "imagecaption",
                        wagtail.core.blocks.StructBlock(
                            [
                                ("image", wagtail.images.blocks.ImageChooserBlock()),
                                ("caption", wagtail.core.blocks.RichTextBlock()),
                            ],
                            label="Image caption",
                        ),
                    ),
                    (
                        "textimage",
                        wagtail.core.blocks.StructBlock(
                            [
                                ("text", wagtail.core.blocks.RichTextBlock()),
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
                        wagtail.core.blocks.StructBlock(
                            [
                                ("text", wagtail.core.blocks.RichTextBlock()),
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
                        wagtail.core.blocks.StructBlock(
                            [
                                ("text", wagtail.core.blocks.RichTextBlock()),
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
                        wagtail.core.blocks.StructBlock(
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
                        wagtail.core.blocks.ListBlock(
                            wagtail.core.blocks.StructBlock(
                                [
                                    (
                                        "image",
                                        wagtail.images.blocks.ImageChooserBlock(),
                                    ),
                                    ("stat", wagtail.core.blocks.CharBlock()),
                                    ("text", wagtail.core.blocks.CharBlock()),
                                ],
                                icon="code",
                            )
                        ),
                    ),
                    (
                        "embed",
                        wagtail.embeds.blocks.EmbedBlock(
                            icon="code",
                            template="patterns/components/streamfields/embed/embed.html",
                        ),
                    ),
                    (
                        "markdown",
                        wagtailio.utils.blocks.MarkDownBlock(
                            template="patterns/components/streamfields/code_block/code_block.html"
                        ),
                    ),
                    (
                        "codeblock",
                        wagtail.core.blocks.StructBlock(
                            [
                                (
                                    "language",
                                    wagtail.core.blocks.ChoiceBlock(
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
                                ("code", wagtail.core.blocks.TextBlock()),
                            ],
                            template="patterns/components/streamfields/code_block/code_block.html",
                        ),
                    ),
                    (
                        "backers",
                        wagtail.core.blocks.StructBlock(
                            [
                                (
                                    "gold_backers",
                                    wagtail.core.blocks.ListBlock(
                                        wagtail.core.blocks.StructBlock(
                                            [
                                                (
                                                    "name",
                                                    wagtail.core.blocks.CharBlock(),
                                                ),
                                                (
                                                    "image",
                                                    wagtail.images.blocks.ImageChooserBlock(
                                                        required=False
                                                    ),
                                                ),
                                                (
                                                    "url",
                                                    wagtail.core.blocks.URLBlock(
                                                        required=False
                                                    ),
                                                ),
                                            ]
                                        )
                                    ),
                                ),
                                (
                                    "silver_backers",
                                    wagtail.core.blocks.ListBlock(
                                        wagtail.core.blocks.StructBlock(
                                            [
                                                (
                                                    "name",
                                                    wagtail.core.blocks.CharBlock(),
                                                ),
                                                (
                                                    "image",
                                                    wagtail.images.blocks.ImageChooserBlock(
                                                        required=False
                                                    ),
                                                ),
                                                (
                                                    "url",
                                                    wagtail.core.blocks.URLBlock(
                                                        required=False
                                                    ),
                                                ),
                                            ]
                                        )
                                    ),
                                ),
                                (
                                    "bronze_backers",
                                    wagtail.core.blocks.ListBlock(
                                        wagtail.core.blocks.StructBlock(
                                            [
                                                (
                                                    "name",
                                                    wagtail.core.blocks.CharBlock(),
                                                ),
                                                (
                                                    "image",
                                                    wagtail.images.blocks.ImageChooserBlock(
                                                        required=False
                                                    ),
                                                ),
                                                (
                                                    "url",
                                                    wagtail.core.blocks.URLBlock(
                                                        required=False
                                                    ),
                                                ),
                                            ]
                                        )
                                    ),
                                ),
                                (
                                    "linked_backers",
                                    wagtail.core.blocks.ListBlock(
                                        wagtail.core.blocks.StructBlock(
                                            [
                                                (
                                                    "name",
                                                    wagtail.core.blocks.CharBlock(),
                                                ),
                                                (
                                                    "url",
                                                    wagtail.core.blocks.URLBlock(
                                                        required=False
                                                    ),
                                                ),
                                            ]
                                        )
                                    ),
                                ),
                                (
                                    "named_backers",
                                    wagtail.core.blocks.ListBlock(
                                        wagtail.core.blocks.StructBlock(
                                            [("name", wagtail.core.blocks.CharBlock())]
                                        )
                                    ),
                                ),
                            ]
                        ),
                    ),
                    (
                        "standalone_cta",
                        wagtail.core.blocks.StructBlock(
                            [
                                (
                                    "cta",
                                    wagtail.core.blocks.StructBlock(
                                        [
                                            (
                                                "text",
                                                wagtail.core.blocks.CharBlock(
                                                    label="CTA text",
                                                    max_length=255,
                                                    required=False,
                                                ),
                                            ),
                                            (
                                                "cta_page",
                                                wagtail.core.blocks.PageChooserBlock(
                                                    label="CTA page", required=False
                                                ),
                                            ),
                                            (
                                                "cta_url",
                                                wagtail.core.blocks.URLBlock(
                                                    label="CTA URL", required=False
                                                ),
                                            ),
                                        ]
                                    ),
                                ),
                                (
                                    "description",
                                    wagtail.core.blocks.TextBlock(
                                        label="Short description",
                                        max_length=100,
                                        required=False,
                                    ),
                                ),
                            ]
                        ),
                    ),
                ]
            ),
        ),
    ]