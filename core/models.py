from django.db import models
from django.utils.text import slugify


class Service(models.Model):
    """Model for freelance services"""
    CATEGORY_CHOICES = [
        ('web', 'Web Design'),
        ('content', 'Content Writing'),
        ('graphic', 'Graphic Design'),
        ('logo', 'Logo Design'),
        ('translation', 'Translation'),
        ('marketing', 'Digital Marketing'),
        ('notes', 'Notes'),
    ]
    
    title = models.CharField(max_length=100)
    description = models.TextField()
    detailed_description = models.TextField(blank=True)
    price_info = models.TextField(blank=True)
    slug = models.SlugField(max_length=100, unique=True, blank=True, null=True)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    icon_class = models.CharField(max_length=50, help_text="FontAwesome icon class (e.g., fas fa-laptop-code)")
    features = models.JSONField(default=list, help_text="List of service features")
    is_active = models.BooleanField(default=True)
    order = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['order', 'title']
    
    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)


class Testimonial(models.Model):
    """Model for client testimonials"""
    client_name = models.CharField(max_length=100)
    client_position = models.CharField(max_length=100)
    client_company = models.CharField(max_length=100)
    content = models.TextField()
    rating = models.IntegerField(choices=[(i, i) for i in range(1, 6)], default=5)
    is_active = models.BooleanField(default=True)
    order = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['order', '-created_at']
    
    def __str__(self):
        return f"{self.client_name} - {self.client_company}"


class About(models.Model):
    """Model for about section content"""
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=200, blank=True)
    content = models.TextField()
    skills = models.JSONField(default=list, help_text="List of skills")
    experience_years = models.IntegerField(default=0)
    projects_completed = models.IntegerField(default=0)
    happy_clients = models.IntegerField(default=0)
    satisfaction_rate = models.IntegerField(default=100)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        # Ensure only one active about section
        if self.is_active:
            About.objects.exclude(pk=self.pk).update(is_active=False)
        super().save(*args, **kwargs)


class SiteSettings(models.Model):
    """Model for site-wide settings"""
    site_name = models.CharField(max_length=100, default="SkillGrid")
    site_description = models.TextField(blank=True)
    hero_title = models.CharField(max_length=200)
    hero_subtitle = models.CharField(max_length=200)
    hero_description = models.TextField()
    contact_email = models.EmailField()
    contact_phone = models.CharField(max_length=20)
    address = models.TextField(blank=True)
    social_facebook = models.URLField(blank=True)
    social_twitter = models.URLField(blank=True)
    social_linkedin = models.URLField(blank=True)
    social_instagram = models.URLField(blank=True)
    social_behance = models.URLField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"Site Settings - {self.site_name}"
    
    def save(self, *args, **kwargs):
        # Ensure only one settings instance
        if not self.pk and SiteSettings.objects.exists():
            return
        super().save(*args, **kwargs)
    
    class Meta:
        verbose_name = "Site Settings"
        verbose_name_plural = "Site Settings" 