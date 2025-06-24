from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.views.generic import TemplateView
from .models import Service, Testimonial, About, SiteSettings
from portfolio.models import Project
from contact.forms import ContactForm
from contact.views import ContactView  # Re-use the email logic


class HomeView(ContactView):
    template_name = 'core/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'services': Service.objects.all().order_by('order'),
            'testimonials': Testimonial.objects.all().order_by('order'),
            'about': About.objects.first(),
            'projects': Project.objects.filter(is_featured=True).order_by('order')[:6],
            'site_settings': SiteSettings.objects.first(),
        })
        # Add daily quote logic
        import datetime
        quotes_list = [
            ("Talk is cheap. Show me the code.", "Linus Torvalds"),
            ("Life is what happens when you're busy making other plans.", "John Lennon"),
            ("I used to think I was indecisive, but now I'm not so sure.", "Anonymous"),
        ]
        day_of_year = datetime.datetime.now().timetuple().tm_yday
        quote, author = quotes_list[day_of_year % len(quotes_list)]
        context['daily_quote'] = quote
        context['daily_author'] = author
        return context

    def post(self, request, *args, **kwargs):
        # This will reuse the same POST handling logic from ContactView
        response = super().post(request, *args, **kwargs)
        # Redirect back to the home page's contact section
        return redirect('core:home' + '#contact')


class AboutView(TemplateView):
    template_name = 'core/about.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['about'] = About.objects.filter(is_active=True).first()
        context['services'] = Service.objects.filter(is_active=True)
        context['site_settings'] = SiteSettings.objects.first()
        return context


class ServicesView(TemplateView):
    template_name = 'core/services.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['services'] = Service.objects.filter(is_active=True)
        context['site_settings'] = SiteSettings.objects.first()
        return context


def service_detail(request, slug):
    service = get_object_or_404(Service, slug=slug, is_active=True)
    settings = SiteSettings.objects.first()
    
    context = {
        'service': service,
        'settings': settings,
    }
    return render(request, 'core/service_detail.html', context)


def about(request):
    about = About.objects.filter(is_active=True).first()
    services = Service.objects.filter(is_active=True)
    settings = SiteSettings.objects.first()
    
    context = {
        'about': about,
        'services': services,
        'site_settings': settings,
    }
    return render(request, 'core/about.html', context) 