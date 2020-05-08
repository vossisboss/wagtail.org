from django.db import models

from wagtail.admin.edit_handlers import FieldPanel, InlinePanel, StreamFieldPanel
from wagtail.core.fields import RichTextField, StreamField
from wagtail.core.models import Page, Orderable
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.snippets.edit_handlers import SnippetChooserPanel
from wagtail.snippets.models import register_snippet
from wagtail_localize.fields import TranslatableField, SynchronizedField
from wagtail_localize.models import TranslatableMixin, TranslatablePageMixin

from modelcluster.fields import ParentalKey
from modelcluster.models import ClusterableModel

from wagtailio.features.blocks import FeatureIndexPageBlock


class Bullet(TranslatableMixin, Orderable):
    snippet = ParentalKey("features.FeatureAspect", related_name="bullets")
    title = models.CharField(max_length=255)
    text = RichTextField()

    panels = [FieldPanel("title"), FieldPanel("text")]

    translatable_fields = [
        TranslatableField('title'),
        TranslatableField('text'),
    ]


@register_snippet
class FeatureAspect(TranslatableMixin, ClusterableModel):
    title = models.CharField(max_length=255)
    video_url = models.URLField(blank=True)
    screenshot = models.ForeignKey(
        "images.WagtailIOImage",
        models.SET_NULL,
        null=True,
        blank=True,
        related_name="+",
    )

    panels = [
        FieldPanel("title"),
        InlinePanel("bullets", label="Bullets"),
        ImageChooserPanel("screenshot"),
        FieldPanel("video_url"),
    ]

    translatable_fields = [
        TranslatableField('title'),
        SynchronizedField('video_url'),
        SynchronizedField('screenshot'),
        TranslatableField('bullets'),
    ]

    def __str__(self):
        return self.title


class FeaturePageFeatureAspect(TranslatableMixin, Orderable):
    page = ParentalKey("features.FeatureDescription", related_name="feature_aspects")
    feature_aspect = models.ForeignKey(
        "features.FeatureAspect", models.CASCADE, related_name="+"
    )

    panels = [SnippetChooserPanel("feature_aspect")]

    translatable_fields = [
        TranslatableField('feature_aspect'),
    ]


@register_snippet
class FeatureDescription(TranslatableMixin, ClusterableModel):
    title = models.CharField(max_length=255)
    introduction = models.CharField(max_length=255, blank=True)
    documentation_link = models.URLField(max_length=255, blank=True)
    panels = [
        FieldPanel("title"),
        FieldPanel("introduction"),
        FieldPanel("documentation_link"),
        InlinePanel("feature_aspects", label="Feature Aspects"),
    ]

    translatable_fields = [
        TranslatableField('title'),
        TranslatableField('introduction'),
        SynchronizedField('documentation_link'),
        SynchronizedField('feature_aspects'),
    ]

    def __str__(self):
        return self.title


class FeatureIndexPageMenuOption(TranslatableMixin, models.Model):
    page = ParentalKey(
        "features.FeatureIndexPage", related_name="secondary_menu_options"
    )
    link = models.ForeignKey("wagtailcore.Page", models.CASCADE, related_name="+")
    label = models.CharField(max_length=255)

    translatable_fields = [
        SynchronizedField('link'),
        TranslatableField('label'),
    ]


class FeatureIndexPage(TranslatablePageMixin, Page):
    body = StreamField(FeatureIndexPageBlock())

    content_panels = Page.content_panels + [StreamFieldPanel("body")]

    translatable_fields = [
        TranslatableField('title'),
        TranslatableField('slug'),
        TranslatableField('seo_title'),
        TranslatableField('search_description'),
        SynchronizedField('show_in_menus'),
        TranslatableField('body'),
        SynchronizedField('secondary_menu_options'),
    ]
