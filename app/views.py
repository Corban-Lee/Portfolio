"""Views for the app."""

# from django.shortcuts import render
from django.views.generic import TemplateView


class IndexView(TemplateView):
    """The landing page for the site."""

    template_name = 'app/index.html'
