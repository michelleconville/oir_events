from django.db import models


class Contact(models.Model):
    first_name = models.CharField(max_length=254, null=True, blank=True)
    last_name = models.CharField(max_length=254, null=True, blank=True)
    phone_number = models.CharField(max_length=16, null=True, blank=True)
    email = models.EmailField(max_length=254, unique=True)
    subject = models.CharField(max_length=255)
    message = models.TextField()

    def __str__(self):
        return self.email
