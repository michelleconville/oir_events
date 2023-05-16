from django.views.generic import TemplateView
from django.shortcuts import render
from .models import CarouselImage


class Index(TemplateView):
    """Display Carousel"""
    template_name = "home/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["carousel_images"] = CarouselImage.objects.all()
        return context
