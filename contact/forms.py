from django import forms
from .models import ContactMessage


class ContactForm(forms.ModelForm):
    """Contact form with enhanced validation"""
    
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'phone_number', 'service', 'budget', 'message']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Your full name'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'your.email@example.com'
            }),
            'phone_number': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Your phone number (optional)'
            }),
            'service': forms.Select(attrs={
                'class': 'form-control'
            }),
            'budget': forms.Select(attrs={
                'class': 'form-control'
            }),
            'message': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 5,
                'placeholder': 'Tell me about your project, goals, and any specific requirements...'
            })
        }
    
    def clean_name(self):
        name = self.cleaned_data.get('name')
        if len(name.strip()) < 2:
            raise forms.ValidationError("Name must be at least 2 characters long.")
        return name.strip()
    
    def clean_message(self):
        message = self.cleaned_data.get('message')
        if len(message.strip()) < 20:
            raise forms.ValidationError("Message must be at least 20 characters long.")
        return message.strip()
    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        # Basic email validation is handled by Django's EmailField
        return email.lower().strip() 