from django.db import models

from modelcluster.models import ClusterableModel
from wagtail.core.fields import StreamField

from wagtail.core.models import Page, Orderable
from wagtail.admin.edit_handlers import StreamFieldPanel
from wagtail_localize.fields import TranslatableField, SynchronizedField
from wagtail_localize.models import TranslatablePageMixin, TranslatablePageRoutingMixin

from wagtailio.blog.models import BlogPage
from wagtailio.core.blocks import HomePageBlock
from wagtailio.utils.models import SocialMediaMixin, CrossPageMixin


class HomePage(TranslatablePageMixin, TranslatablePageRoutingMixin, SocialMediaMixin, CrossPageMixin, Page):
    body = StreamField(HomePageBlock())
    parent_page_types = ["wagtailcore.Page"]
    subpage_types = [
        "blog.BlogIndexPage",
        "developers.DevelopersPage",
        "features.FeatureIndexPage",
        "newsletter.NewsletterIndexPage",
        "standardpage.StandardPage",
    ]
    content_panels = Page.content_panels + [StreamFieldPanel("body")]

    promote_panels = (
        Page.promote_panels + SocialMediaMixin.panels + CrossPageMixin.panels
    )


    translatable_fields = SocialMediaMixin.translatable_fields + CrossPageMixin.translatable_fields + [
        TranslatableField('title'),
        TranslatableField('slug'),
        TranslatableField('seo_title'),
        TranslatableField('search_description'),
        SynchronizedField('show_in_menus'),
        TranslatableField('body'),
    ]

    def get_context(self, request, *args, **kwargs):
        context = super(HomePage, self).get_context(request, *args, **kwargs)
        context.update({"blog_posts": BlogPage.objects.live().order_by("-date")})

        return context
