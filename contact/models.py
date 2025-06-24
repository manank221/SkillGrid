from django.db import models


class ContactMessage(models.Model):
    """Model for contact form messages"""
    SERVICE_CHOICES = [
        ('web-design', 'Web Design'),
        ('content-writing', 'Content Writing'),
        ('graphic-design', 'Graphic Design'),
        ('logo-design', 'Logo Design'),
        ('translation', 'Translation'),
        ('counselling', 'Counselling'),
        ('other', 'Other'),
    ]
    
    BUDGET_CHOICES = [
        ('under-500', 'Under $500'),
        ('500-1000', '$500 - $1,000'),
        ('1000-2500', '$1,000 - $2,500'),
        ('2500-5000', '$2,500 - $5,000'),
        ('over-5000', 'Over $5,000'),
    ]
    
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20, blank=True)
    service = models.CharField(max_length=20, choices=SERVICE_CHOICES)
    budget = models.CharField(max_length=20, choices=BUDGET_CHOICES, blank=True)
    message = models.TextField()
    ip_address = models.GenericIPAddressField(blank=True, null=True)
    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return f"{self.name} - {self.service} - {self.created_at.strftime('%Y-%m-%d')}" 