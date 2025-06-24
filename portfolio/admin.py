from django.contrib import admin
from .models import Project, ProjectImage


class ProjectImageInline(admin.TabularInline):
    model = ProjectImage
    extra = 1


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'client', 'is_featured', 'is_active', 'order', 'created_at']
    list_filter = ['category', 'is_featured', 'is_active', 'completion_date', 'created_at']
    list_editable = ['is_featured', 'is_active', 'order']
    search_fields = ['title', 'description', 'client']
    prepopulated_fields = {'slug': ('title',)}
    ordering = ['order', '-created_at']
    inlines = [ProjectImageInline]
    readonly_fields = ['created_at', 'updated_at']


@admin.register(ProjectImage)
class ProjectImageAdmin(admin.ModelAdmin):
    list_display = ['project', 'caption', 'order', 'created_at']
    list_filter = ['project', 'created_at']
    list_editable = ['order']
    search_fields = ['project__title', 'caption']
    ordering = ['project', 'order'] 