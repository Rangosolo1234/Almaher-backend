from django.db import models

class Inquiry(models.Model):
    GENERAL = "general"
    PHOTOGRAPHER = "photographer"
    PARTNERSHIP = "partnership"
    TYPES = [
        (GENERAL, "General"),
        (PHOTOGRAPHER, "Photographer"),
        (PARTNERSHIP, "Partnership"),
    ]

    category = models.CharField(max_length=20, choices=TYPES)
    organization_name = models.CharField(max_length=255, blank=True, null=True)
    organization_website = models.URLField( blank=True, null=True)
    portfolio_link = models.URLField(blank=True,null=True)
    name = models.CharField(max_length=255)
    email = models.EmailField()
    country = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.category} - {self.name}"