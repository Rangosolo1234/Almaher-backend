from django.db import models

class Nomination(models.Model):
    full_name = models.CharField(max_length=255)
    country = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    what_she_is_doing = models.TextField()
    submitted_by_name = models.CharField(max_length=255)
    submitted_by_email = models.EmailField()
    reviewed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name