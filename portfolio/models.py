from django.db import models
from django.utils.text import slugify


class Project(models.Model):
    """Model for portfolio projects"""
    CATEGORY_CHOICES = [
        ('web', 'Web Design'),
        ('graphic', 'Graphic Design'),
        ('content', 'Content Writing'),
        ('logo', 'Logo Design'),
        ('translation', 'Translation'),
        ('marketing', 'Digital Marketing'),
    ]
    
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True, blank=True)
    description = models.TextField()
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    client = models.CharField(max_length=100, blank=True)
    project_url = models.URLField(blank=True)
    completion_date = models.DateField(blank=True, null=True)
    image = models.ImageField(upload_to='portfolio/', blank=True, null=True)
    technologies_used = models.JSONField(default=list, help_text="List of technologies used")
    is_featured = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    order = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['order', '-created_at']
    
    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)
    
    def get_absolute_url(self):
        return f'/portfolio/{self.slug}/'


class ProjectImage(models.Model):
    """Model for additional project images"""
    project = models.ForeignKey(Project, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='portfolio/images/')
    caption = models.CharField(max_length=200, blank=True)
    order = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['order', 'created_at']
    
    def __str__(self):
        return f"{self.project.title} - {self.caption or 'Image'}" 