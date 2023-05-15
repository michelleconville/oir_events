from django.db import models


class Contact(models.Model):
    """
    Model to create a contact form
    """
    name = models.CharField(max_length=254, null=True, blank=False)
    email = models.EmailField(max_length=254, unique=False)
    message = models.TextField()
    posted_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.name)
