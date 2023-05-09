from django.db import models


class Contact(models.Model):
    name = models.CharField(max_length=254, null=True, blank=True)
    email = models.EmailField(max_length=254, unique=True)
    message = models.TextField()
    posted_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.name)
