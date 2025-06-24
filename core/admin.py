from django.contrib import admin
from .models import Service, Testimonial, About, SiteSettings


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'is_active', 'order', 'created_at']
    list_filter = ['category', 'is_active', 'created_at']
    list_editable = ['is_active', 'order']
    search_fields = ['title', 'description']
    ordering = ['order', 'title']


@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ['client_name', 'client_company', 'rating', 'is_active', 'order', 'created_at']
    list_filter = ['rating', 'is_active', 'created_at']
    list_editable = ['is_active', 'order', 'rating']
    search_fields = ['client_name', 'client_company', 'content']
    ordering = ['order', '-created_at']


@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ['title', 'experience_years', 'projects_completed', 'happy_clients', 'is_active']
    list_editable = ['is_active']
    search_fields = ['title', 'content']
    
    def has_add_permission(self, request):
        # Only allow one about section
        return not About.objects.exists()


@admin.register(SiteSettings)
class SiteSettingsAdmin(admin.ModelAdmin):
    list_display = ['site_name', 'contact_email', 'contact_phone', 'updated_at']
    search_fields = ['site_name', 'contact_email']
    
    def has_add_permission(self, request):
        # Only allow one settings instance
        return not SiteSettings.objects.exists()
    
    def has_delete_permission(self, request, obj=None):
        # Prevent deletion of settings
        return False 