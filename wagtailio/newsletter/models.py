from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db import models
from django.shortcuts import render

from wagtail.admin.edit_handlers import FieldPanel
from wagtail.core.fields import RichTextField
from wagtail.core.models import Page
from wagtail_localize.fields import TranslatableField, SynchronizedField
from wagtail_localize.models import TranslatablePageMixin


class NewsletterPage(TranslatablePageMixin, Page):
    date = models.DateField("Newsletter date")
    intro = RichTextField(blank=True)
    body = RichTextField()

    content_panels = Page.content_panels + [
        FieldPanel("date"),
        FieldPanel("intro", classname="full"),
        FieldPanel("body", classname="full"),
    ]

    translatable_fields = [
        TranslatableField('title'),
        TranslatableField('slug'),
        TranslatableField('seo_title'),
        TranslatableField('search_description'),
        SynchronizedField('show_in_menus'),
        SynchronizedField('date'),
        TranslatableField('intro'),
        TranslatableField('body'),
    ]

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        if request.GET.get("email", "false") == "true":
            context["is_email"] = True

        return context


class NewsletterIndexPage(TranslatablePageMixin, Page):
    intro = RichTextField(blank=True)
    body = RichTextField()

    @property
    def newsletters(self):
        # Get list of blog pages that are descendants of this page
        newsletters = NewsletterPage.objects.live().descendant_of(self)

        # Order by most recent date first
        newsletters = newsletters.order_by("-date")

        return newsletters

    def serve(self, request):
        # Get blogs
        newsletters = self.newsletters

        # Pagination
        page = request.GET.get("page")
        paginator = Paginator(newsletters, 5)  # Show 5 blogs per page
        try:
            newsletters = paginator.page(page)
        except PageNotAnInteger:
            newsletters = paginator.page(1)
        except EmptyPage:
            newsletters = paginator.page(paginator.num_pages)

        return render(
            request, self.template, {"self": self, "newsletters": newsletters}
        )

    content_panels = Page.content_panels + [
        FieldPanel("intro", classname="full"),
        FieldPanel("body", classname="full"),
    ]

    translatable_fields = [
        TranslatableField('title'),
        TranslatableField('slug'),
        TranslatableField('seo_title'),
        TranslatableField('search_description'),
        SynchronizedField('show_in_menus'),
        TranslatableField('intro'),
        TranslatableField('body'),
    ]


class NewsletterEmailAddress(models.Model):
    email = models.EmailField()
