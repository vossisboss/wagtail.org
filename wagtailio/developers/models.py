from django.db import models

from modelcluster.fields import ParentalKey
from wagtail.admin.edit_handlers import (
    FieldPanel,
    InlinePanel,
    MultiFieldPanel,
    PageChooserPanel,
    StreamFieldPanel,
)
from wagtail.core.fields import StreamField
from wagtail.core.models import Orderable, Page
from wagtail_localize.fields import TranslatableField, SynchronizedField
from wagtail_localize.models import TranslatableMixin, TranslatablePageMixin

from wagtailio.core.blocks import CodePromoBlock
from wagtailio.utils.models import CrossPageMixin, SocialMediaMixin


class DevelopersPageOptions(TranslatableMixin, Orderable):
    page = ParentalKey("developers.DevelopersPage", related_name="options")
    icon = models.CharField(
        max_length=255,
        choices=(
            ("github", "Github"),
            ("social", "Social"),
            ("documentation", "Documentation"),
        ),
    )
    title = models.CharField(max_length=255)
    summary = models.CharField(max_length=255)
    internal_link = models.ForeignKey(
        "wagtailcore.Page", models.CASCADE, null=True, blank=True, related_name="+"
    )
    external_link = models.URLField("External link", blank=True)

    @property
    def link(self):
        if self.internal_link:
            return self.internal_link.url
        else:
            return self.external_link

    panels = [
        FieldPanel("icon"),
        FieldPanel("title"),
        FieldPanel("summary"),
        MultiFieldPanel(
            [PageChooserPanel("internal_link"), FieldPanel("external_link")], "Link"
        ),
    ]

    translatable_fields = [
        SynchronizedField('icon'),
        TranslatableField('title'),
        TranslatableField('summary'),
        SynchronizedField('internal_link'),
        SynchronizedField('iconexternal_link'),
    ]


class DevelopersPage(TranslatablePageMixin, SocialMediaMixin, CrossPageMixin, Page):
    body = StreamField(
        (
            (
                "code",
                CodePromoBlock(template="developers/blocks/code_with_link_block.html"),
            ),
        )
    )

    content_panels = Page.content_panels + [
        StreamFieldPanel("body"),
        InlinePanel("options", label="Options"),
    ]

    translatable_fields = SocialMediaMixin.translatable_fields + CrossPageMixin.translatable_fields + [
        TranslatableField('title'),
        TranslatableField('slug'),
        TranslatableField('seo_title'),
        TranslatableField('search_description'),
        SynchronizedField('show_in_menus'),
        TranslatableField('body'),
        TranslatableField('options'),
    ]
