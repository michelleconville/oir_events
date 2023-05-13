from django.test import TestCase
from django.urls import reverse
from .models import CarouselImage


class HomepageTestCase(TestCase):
    """ Homepage opens """
    def test_homepage(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)


class CarouselImageTestCase(TestCase):
    """ Retrieving carousel images """
    def setUp(self):
        CarouselImage.objects.create(
            image="path/to/image1.jpg",
            caption="Image 1",
            description="Description 1",
            cta_text="CTA 1",
            cta_url="https://example.com"
        )
        CarouselImage.objects.create(
            image="path/to/image2.jpg",
            caption="Image 2",
            description="Description 2",
            cta_text="CTA 2",
            cta_url="https://example.com"
        )

    def test_carousel_images_count(self):
        carousel_images = CarouselImage.objects.all()
        self.assertEqual(carousel_images.count(), 2)

    def test_carousel_image_fields(self):
        carousel_image = CarouselImage.objects.first()
        self.assertEqual(carousel_image.caption, "Image 1")
        self.assertEqual(carousel_image.description, "Description 1")
        self.assertEqual(carousel_image.cta_text, "CTA 1")
        self.assertEqual(carousel_image.cta_url, "https://example.com")

    def test_index_view(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "home/index.html")
        self.assertEqual(len(response.context["carousel_images"]), 2)
