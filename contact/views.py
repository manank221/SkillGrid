from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from django.views.generic import TemplateView
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from .forms import ContactForm
from .models import ContactMessage
from core.models import SiteSettings
import logging

# Configure logging
logger = logging.getLogger(__name__)

class ContactView(TemplateView):
    template_name = 'contact/contact.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = ContactForm()
        context['site_settings'] = SiteSettings.objects.first()
        return context
    
    def post(self, request, *args, **kwargs):
        form = ContactForm(request.POST)
        context = self.get_context_data()
        context['form'] = form
        
        if form.is_valid():
            contact_message = form.save(commit=False)
            contact_message.ip_address = self.get_client_ip(request)
            contact_message.save()
            
            try:
                self.send_email_notification(contact_message)
                messages.success(request, 'Thank you! Your message has been sent successfully.')
            except Exception as e:
                messages.error(request, f'There was an error sending your message. Please check your settings. Error: {e}')
            
            return redirect('contact:contact')
        
        return render(request, self.template_name, context)
    
    def get_client_ip(self, request):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        return ip
    
    def send_email_notification(self, contact_message):
        """Send email notification to admin"""
        site_settings = SiteSettings.objects.first()
        if not site_settings or not site_settings.contact_email:
            logger.warning("Admin contact email not set. Skipping email notification.")
            return
        
        subject = f'New Contact Form Submission - {contact_message.service}'
        message = f"""
New contact form submission received:

Name: {contact_message.name}
Email: {contact_message.email}
Phone: {contact_message.phone_number if contact_message.phone_number else 'Not provided'}
Service: {contact_message.get_service_display()}
Budget: {contact_message.get_budget_display() if contact_message.budget else 'Not specified'}

Message:
{contact_message.message}

Submitted at: {contact_message.created_at}
IP Address: {contact_message.ip_address}
        """
        
        send_mail(
            subject=subject,
            message=message,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[site_settings.contact_email],
            fail_silently=False,
        )

@csrf_exempt
def contact_ajax(request):
    """AJAX endpoint for contact form submission"""
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            contact_message = form.save(commit=False)
            contact_message.ip_address = request.META.get('REMOTE_ADDR')
            contact_message.save()
            
            # Use the main view's methods to send notifications
            view = ContactView()
            try:
                view.send_email_notification(contact_message)
                return JsonResponse({
                    'success': True,
                    'message': 'Thank you! Your message has been sent successfully.'
                })
            except Exception as e:
                logger.error(f"Failed to send notification from AJAX view: {e}")
                return JsonResponse({
                    'success': False,
                    'message': f'Your message was saved, but there was an error sending notifications. Please contact the administrator. Error: {e}'
                })
        else:
            return JsonResponse({'success': False, 'errors': form.errors})
    
    return JsonResponse({'success': False, 'message': 'Invalid request method'}) 