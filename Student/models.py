"""Accounts app models."""

from django.db import models


class upload(models.Model):
    """Upload model."""

    name = models.CharField(max_length=100)
    image = models.FileField(upload_to="uploads/",)
    year = models.CharField(max_length=100)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Return name of the file."""
        return self.name
