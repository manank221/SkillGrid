from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from django.db.models import Q
from .models import Project
from core.models import SiteSettings


class PortfolioListView(ListView):
    model = Project
    template_name = 'portfolio/portfolio_list.html'
    context_object_name = 'projects'
    paginate_by = 9
    
    def get_queryset(self):
        queryset = Project.objects.filter(is_active=True)
        category = self.request.GET.get('category')
        if category:
            queryset = queryset.filter(category=category)
        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Project.CATEGORY_CHOICES
        context['current_category'] = self.request.GET.get('category', '')
        context['site_settings'] = SiteSettings.objects.first()
        return context


class ProjectDetailView(DetailView):
    model = Project
    template_name = 'portfolio/project_detail.html'
    context_object_name = 'project'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['site_settings'] = SiteSettings.objects.first()
        # Get related projects from the same category
        context['related_projects'] = Project.objects.filter(
            category=self.object.category,
            is_active=True
        ).exclude(pk=self.object.pk)[:3]
        return context 