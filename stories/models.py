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


class StorySection(models.Model):
    LAYOUT_CHOICES = [
        ("text_left", "Text Left / Image Right"),
        ("text_right", "Image Left / Text Right"),
        ("full_width", "Full Width"),
        ("image_grid", "Image Grid"),
    ]

    story = models.ForeignKey(Story, on_delete=models.CASCADE, related_name="sections")
    heading = models.CharField(max_length=255, blank=True)
    content = models.TextField()
    layout = models.CharField(max_length=30, choices=LAYOUT_CHOICES,default="text_left")
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["order", "id"]

    def __str__(self):
        if self.heading:
            return f"{self.story.woman_name} - {self.heading}"
        
        return f"{self.story.woman_name} - Section {self.order}"

class StorySectionImage(models.Model):
    section = models.ForeignKey(StorySection, on_delete=models.CASCADE, related_name="images")
    image = CloudinaryField("image", folder="almaher/stories")
    caption = models.CharField(max_length=255, blank=True)
    alt_text = models.CharField(max_length=255, blank=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["order", "id"]

    def __str__(self):
        return f"{self.section} - Image {self.order}"