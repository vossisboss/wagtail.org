from django.db import models

from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel
from wagtail.core.fields import StreamField
from wagtail.core.models import Page
from wagtail_localize.fields import TranslatableField, SynchronizedField
from wagtail_localize.models import TranslatablePageMixin

from wagtailio.utils.blocks import StoryBlock
from wagtailio.utils.models import CrossPageMixin, SocialMediaMixin


class StandardPage(TranslatablePageMixin, SocialMediaMixin, CrossPageMixin, Page):
    introduction = models.CharField(max_length=511)
    body = StreamField(StoryBlock())

    content_panels = Page.content_panels + [
        FieldPanel("introduction"),
        StreamFieldPanel("body"),
    ]

    promote_panels = (
        Page.promote_panels + SocialMediaMixin.panels + CrossPageMixin.panels
    )

    translatable_fields = SocialMediaMixin.translatable_fields + CrossPageMixin.translatable_fields + [
        TranslatableField('title'),
        TranslatableField('slug'),
        TranslatableField('seo_title'),
        TranslatableField('search_description'),
        SynchronizedField('show_in_menus'),
        TranslatableField('introduction'),
        TranslatableField('body'),
    ]
