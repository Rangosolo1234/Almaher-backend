# from django.contrib.gis.db import models
from django.db import models
from django.utils.text import slugify
from cloudinary.models import CloudinaryField


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Story(models.Model):
    title = models.CharField(max_length=255)
    woman_name = models.CharField(max_length=255)
    quote = models.TextField()
    summary = models.TextField()
    story_content = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    country = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    location = models.CharField(max_length=100, null=True, blank=True)
    read_time = models.PositiveIntegerField(default=5)
    featured = models.BooleanField(default=False)
    hero_story = models.BooleanField(default=False)
    cover_image = CloudinaryField("cover_image", folder="almaher/stories", null=True, blank=True)
    slug = models.SlugField(unique=True,blank=True)
    published_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(
                f"{self.woman_name}-{self.title}"
            )

        super().save(*args, **kwargs)

    def __str__(self):
        return self.woman_name